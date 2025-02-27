from collections import defaultdict

def if_contains_anagrams(strings):
    count = defaultdict(int)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        count[sorted_s] += 1
    pairs = sum((v // 2 for v in count.values()))
    return pairs >= 6