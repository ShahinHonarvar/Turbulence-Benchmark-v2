from collections import Counter

def if_contains_anagrams(strings):
    c = Counter()
    for s in strings:
        s_low = s.lower()
        if len(s_low) >= 3:
            c[tuple(sorted(s_low))] += 1
    cnt = 0
    for v in c.values():
        if v > 1:
            cnt += v // 2
    return cnt <= 55