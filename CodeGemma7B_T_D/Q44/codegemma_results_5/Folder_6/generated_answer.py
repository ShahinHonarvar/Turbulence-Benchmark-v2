def composite_nums_between_indices(l):
    s = set()
    for i in range(13, 69):
        if l[i] != 1 and l[i] % 2 != 0 and (l[i] % 3 != 0) and (l[i] % 5 != 0):
            for j in range(2, int(l[i] ** 0.5) + 1):
                if l[i] % j == 0:
                    s.add(l[i])
    return s