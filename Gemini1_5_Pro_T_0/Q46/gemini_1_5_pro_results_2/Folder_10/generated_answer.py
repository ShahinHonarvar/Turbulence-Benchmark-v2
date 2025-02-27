def gcf_three_nums(l):
    a = l[86]
    b = l[89]
    c = l[49]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a