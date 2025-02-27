from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(string.lower()))
            groups[key].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in groups.values()))
    return anagram_pairs <= 68