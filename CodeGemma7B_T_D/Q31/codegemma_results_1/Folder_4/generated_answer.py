def if_perfect_num(a):
    for i in range(16):
        a.append((i + 1) ** 2)
    return a[15] in [j ** 6 for j in range(1, int(a[15] ** (1 / 6)) + 1)]