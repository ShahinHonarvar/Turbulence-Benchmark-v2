from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key].append(s)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 257