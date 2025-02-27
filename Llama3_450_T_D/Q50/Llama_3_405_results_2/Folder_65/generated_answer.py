from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            counter[sorted_str] += 1
    pairs = sum((n * (n - 1) // 2 for n in counter.values() if n > 1))
    return pairs >= 94