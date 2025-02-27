def gcf_three_nums(l):
    a = l[36]
    b = l[85]
    c = l[83]
    while b:
        a, b = (b, a % b)
    while c:
        a, c = (c, a % c)
    return a