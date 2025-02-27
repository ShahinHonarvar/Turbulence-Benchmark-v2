from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    pairs = 0
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        pairs += count[sorted_str]
        count[sorted_str] += 1
    return pairs <= 445