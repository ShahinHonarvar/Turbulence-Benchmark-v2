from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_str) >= 3:
            anagram_groups[sorted_str].append(string)
    anagram_pairs = sum((len(vals) * (len(vals) - 1) // 2 for vals in anagram_groups.values()))
    return anagram_pairs <= 96