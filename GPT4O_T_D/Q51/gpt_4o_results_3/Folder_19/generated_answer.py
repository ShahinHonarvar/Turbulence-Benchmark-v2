from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    processed_strings = [''.join(filter(str.isalpha, s.lower())) for s in strings if len(s) >= 3]
    anagram_dict = defaultdict(list)
    for string in processed_strings:
        sorted_str = ''.join(sorted(string))
        anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for candidates in anagram_dict.values():
        n = len(candidates)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 69:
            return False
    return True