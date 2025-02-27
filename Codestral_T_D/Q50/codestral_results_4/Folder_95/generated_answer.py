from collections import Counter

def if_contains_anagrams(strings):
    counter = Counter()
    for s in strings:
        key = ''.join(sorted(s.lower()))
        if len(key) >= 3:
            counter[key] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) >= 93