from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            anagrams[key] += 1
    return sum((n * (n - 1) // 2 for n in anagrams.values())) <= 72