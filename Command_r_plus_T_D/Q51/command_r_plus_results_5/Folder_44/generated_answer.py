def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text.lower() if e.isalpha()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1, str2 = (lst[i], lst[j])
            if len(str1) < 3 or len(str2) < 3:
                continue
            normalized1, normalized2 = (normalize_text(str1), normalize_text(str2))
            if normalized1 == normalized2 and (normalized1, normalized2) not in anagram_pairs:
                anagram_count += 1
                anagram_pairs.add((normalized1, normalized2))
                if anagram_count > 75:
                    return False
    return True