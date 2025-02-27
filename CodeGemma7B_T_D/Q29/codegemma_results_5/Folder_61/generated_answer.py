def gcf_two_nums(a):
    x = a[8]
    y = a[3]
    while y:
        x, y = (y, x % y)
    return x