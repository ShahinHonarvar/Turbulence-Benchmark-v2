from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_dict[sorted_str].append(string)
    anagram_pairs = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            n = len(anagram_group)
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs >= 7