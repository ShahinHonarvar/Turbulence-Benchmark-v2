from collections import defaultdict

def if_contains_anagrams(lst):
    chk = defaultdict(int)
    for i in lst:
        if len(i) >= 3:
            i = i.lower()
            chk[sorted(i)] += 1
    length = len(chk)
    return length <= 86