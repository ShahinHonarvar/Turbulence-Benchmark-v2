from collections import defaultdict

def if_contains_anagrams(strings):
    counter = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        counter[sorted_str] += 1
    pairs = sum((n * (n - 1) // 2 for n in counter.values()))
    return pairs <= 10