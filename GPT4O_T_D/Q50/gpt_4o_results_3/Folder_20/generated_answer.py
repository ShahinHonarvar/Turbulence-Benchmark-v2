from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams[sorted_s] += 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count >= 64