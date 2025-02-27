from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string].append(string)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) >= 2))
    return pairs >= 189