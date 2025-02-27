from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    ans = 0
    for s in lst:
        s = s.lower()
        if len(s) >= 3 and s.isalpha():
            s = ''.join(sorted(s))
            c[s] += 1
            if c[s] > 1:
                ans += 1
    return ans <= 30