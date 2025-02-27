def gcf_two_nums(l):
    a = l[84]
    b = l[13]
    while b > 0:
        a, b = (b, a % b)
    return a