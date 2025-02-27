from collections import Counter

def if_contains_anagrams(s):
    c = 0
    d = {}
    for i in s:
        if len(i) >= 3:
            i = i.lower()
            a = Counter(i)
            if str(a) not in d:
                d[str(a)] = i
            else:
                c += 1
                d[str(a)] = ''
    if c > 11:
        return True
    else:
        return False