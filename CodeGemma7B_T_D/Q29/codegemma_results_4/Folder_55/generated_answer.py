def gcf_two_nums(a):
    g = max(a[2], a[1])
    for i in range(g, 0, -1):
        if a[2] % i == 0 and a[1] % i == 0:
            return i