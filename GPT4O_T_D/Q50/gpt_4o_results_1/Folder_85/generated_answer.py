from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            anagram_dict[''.join(sorted(string.lower()))].append(string)
    pair_count = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            pair_count += n * (n - 1) // 2
    return pair_count >= 73