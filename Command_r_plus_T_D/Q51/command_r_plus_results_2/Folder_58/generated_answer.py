def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(normalize_text(lst[i]), normalize_text(lst[j])):
                anagram_pairs += 1
                if anagram_pairs > 60:
                    return False
    return True