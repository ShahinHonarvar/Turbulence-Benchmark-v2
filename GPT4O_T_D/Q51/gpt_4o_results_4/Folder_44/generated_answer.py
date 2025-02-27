from collections import defaultdict

def if_contains_anagrams(strings):
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted((c.lower() for c in s if c.isalpha())))
            counts[sorted_s] += 1
    pairs = sum((k * (k - 1) // 2 for k in counts.values()))
    return pairs <= 75