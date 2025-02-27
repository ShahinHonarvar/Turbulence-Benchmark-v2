def all_even_ints_inclusive(f):
    a = []
    for i in range(15, 40):
        if f[i] % 2 == 0:
            a.append(f[i])
    if len(a) == 0:
        return []
    return a