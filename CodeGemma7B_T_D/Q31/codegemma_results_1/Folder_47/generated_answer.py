def if_perfect_num(a):
    if len(a) <= 34:
        return False
    s = 0
    for i in range(1, a[34] + 1):
        if a[34] % i == 0:
            s += i
    return s == a[34] + 1