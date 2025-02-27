def if_perfect_num(a):
    if len(a) < 34:
        return false
    if a[33] % int(a[33] / 2) == 0:
        return true
    else:
        return false