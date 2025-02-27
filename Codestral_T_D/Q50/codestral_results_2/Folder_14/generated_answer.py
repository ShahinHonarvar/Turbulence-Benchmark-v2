from collections import defaultdict

def if_contains_anagrams(strings):
    groups = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            groups[key].append(s)
    anagram_pairs = [len(v) for v in groups.values() if len(v) >= 2]
    return sum(anagram_pairs) >= 22