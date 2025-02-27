from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        key = ''.join(sorted(string.lower()))
        anagram_groups[key].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values() if len(group[0]) >= 3))
    return anagram_pairs >= 35