def all_even_ints_exclusive(lst):
    l = []
    for i in range(20, 200):
        if lst[i] % 2 == 0:
            l.append(lst[i])
    if len(l) == 0:
        return []
    return l