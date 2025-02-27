from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            canonical = sorted_string(s)
            counts[canonical] += 1
    pairs = 0
    for c in counts.values():
        pairs += c * (c - 1) // 2
        if pairs >= 6:
            return True
    return False