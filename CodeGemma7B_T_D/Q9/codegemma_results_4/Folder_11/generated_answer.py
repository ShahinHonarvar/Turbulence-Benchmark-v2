def all_odd_ints_inclusive(a):
    l = []
    for i in a:
        if i % 2 == 1 and 37 <= i <= 51:
            l.append(i)
    if len(l) != 0:
        return l
    return []