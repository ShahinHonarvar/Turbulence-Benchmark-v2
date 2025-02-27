from collections import Counter

def if_contains_anagrams(lst):
    cnt = Counter()
    ans = 0
    for s in lst:
        if len(s) < 3:
            continue
        s = s.replace(' ', '').lower()
        cnt[tuple(sorted(s))] += 1
        if cnt[tuple(sorted(s))] % 2 == 0:
            ans += 1
    return ans <= 93