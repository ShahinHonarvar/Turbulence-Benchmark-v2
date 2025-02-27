from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return pairs >= 54