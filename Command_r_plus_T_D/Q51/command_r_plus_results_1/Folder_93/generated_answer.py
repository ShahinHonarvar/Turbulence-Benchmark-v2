def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = normalize_text(lst[i])
            str2 = normalize_text(lst[j])
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_key = tuple(sorted((str1, str2)))
                if anagram_key not in anagram_set:
                    anagram_set.add(anagram_key)
                    anagram_count += 1
                    if anagram_count > 36:
                        return False
    return True