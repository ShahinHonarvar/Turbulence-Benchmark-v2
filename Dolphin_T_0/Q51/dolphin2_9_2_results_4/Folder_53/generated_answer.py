def if_contains_anagrams(lst):
    lst2 = [i.lower() for i in lst]
    c = {}
    for i in lst2:
        if len(i) >= 3:
            if sorted(i) in c:
                c[sorted(i)] += 1
            else:
                c[sorted(i)] = 1
    if c.values():
        return max(c.values()) <= 8
    else:
        return False