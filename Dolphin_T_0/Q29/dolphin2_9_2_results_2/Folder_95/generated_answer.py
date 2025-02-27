def gcf_two_nums(l):
    a, b = (l[43], l[99])
    while b != 0:
        a %= b
        a, b = (b, a)
    return a