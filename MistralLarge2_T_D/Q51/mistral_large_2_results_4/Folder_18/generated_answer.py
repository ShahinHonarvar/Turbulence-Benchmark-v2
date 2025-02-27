from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagrams[sorted_str].append(s)
    count = sum((len(group) >= 2 for group in anagrams.values()))
    return count <= 42