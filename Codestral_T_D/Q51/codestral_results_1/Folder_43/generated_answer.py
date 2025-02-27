from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            groups[key].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in groups.values()))
    return anagram_pairs <= 3