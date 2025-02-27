def all_even_ints_inclusive(l):
    a = []
    for i in range(66, 94):
        if i >= len(l):
            break
        if l[i] % 2 == 0:
            a.append(l[i])
    return a