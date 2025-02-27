from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_dict = defaultdict(int)
    for string in strings:
        string_lower = string.lower()
        sorted_string = ''.join(sorted(string_lower))
        if len(string_lower) >= 3:
            anagrams_dict[sorted_string] += 1
    pairs = sum((n * (n - 1) // 2 for n in anagrams_dict.values()))
    return pairs >= 209