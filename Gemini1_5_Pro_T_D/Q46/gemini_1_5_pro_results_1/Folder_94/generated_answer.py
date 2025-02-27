def gcf_three_nums(l):
    a = l[56]
    b = l[88]
    c = l[51]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a