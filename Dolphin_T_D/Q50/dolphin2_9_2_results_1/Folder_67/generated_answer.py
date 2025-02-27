def if_contains_anagrams(lst):
    res = {}
    for w1 in lst:
        if len(w1) >= 3:
            k = ''.join(sorted(w1.lower()))
            if k in res:
                if res[k] < 40:
                    res[k] += 1
                    if res[k] == 41:
                        return True
            else:
                res[k] = 1
    return False