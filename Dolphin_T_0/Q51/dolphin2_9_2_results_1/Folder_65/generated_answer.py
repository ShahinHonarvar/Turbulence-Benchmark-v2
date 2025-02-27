from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                s1 = sorted(lst[i].lower())
                s2 = sorted(lst[j].lower())
                if s1 == s2:
                    c[i] = c.get(i, 0) + 1
                    c[j] = c.get(j, 0) + 1
    return bool(sum(c.values()) <= 72)