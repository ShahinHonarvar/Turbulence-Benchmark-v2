def all_odd_ints_exclusive(a):
    b = []
    while 29 <= len(b) < 53:
        if a[len(b)] % 2 != 0:
            b.append(a[len(b)])
    return b