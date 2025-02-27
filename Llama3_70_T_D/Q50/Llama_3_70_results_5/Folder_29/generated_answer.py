from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            anagrams[s] += 1
    count = sum((1 for v in anagrams.values() if v > 1))
    return count >= 35