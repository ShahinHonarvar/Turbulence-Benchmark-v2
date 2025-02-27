from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            counts[sorted_s] += 1
    pairs = sum((c * (c - 1) // 2 for c in counts.values()))
    return pairs <= 279