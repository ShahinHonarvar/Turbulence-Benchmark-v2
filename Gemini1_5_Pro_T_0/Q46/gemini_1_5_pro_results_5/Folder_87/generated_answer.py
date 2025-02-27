def gcf_three_nums(l):
    a = l[74]
    b = l[60]
    c = l[28]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a