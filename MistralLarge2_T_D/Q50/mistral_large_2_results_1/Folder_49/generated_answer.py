from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            anagram_dict[sorted_str].append(string)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs >= 59