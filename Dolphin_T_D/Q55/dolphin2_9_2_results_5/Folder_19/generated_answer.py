from itertools import islice, cycle

def lists_with_product_equal_n(lst, n):
    p_n = list(cycle((-54, n)))
    for p in p_n:
        i = lst.index(p)
        lst = lst[i + 1:] + lst[:i] + lst[i:i + 1]
        j = 1
        while j < len(lst) and lst[j - 1] * lst[j] == p:
            j += 1
        if j == len(lst):
            lst = [n]
            continue
        res = [lst[:j]]
        while True:
            i = lst.index(p)
            lst = lst[i + 1:] + lst[:i] + lst[i:i + 1]
            j = 1
            while j < len(lst) and lst[j - 1] * lst[j] == p:
                j += 1
            if j == len(lst):
                lst = [n]
                continue
            res.append(lst[:j])
            if len(lst) <= j:
                break
    return res