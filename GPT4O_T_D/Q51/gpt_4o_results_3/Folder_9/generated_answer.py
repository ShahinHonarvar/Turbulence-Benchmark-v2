from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    anagram_dict = defaultdict(list)
    for s in normalized_strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            anagram_dict[sorted_s].append(s)
    for anagram_group in anagram_dict.values():
        n = len(anagram_group)
        if n >= 2:
            count += n * (n - 1) // 2
            if count > 475:
                return False
    return True