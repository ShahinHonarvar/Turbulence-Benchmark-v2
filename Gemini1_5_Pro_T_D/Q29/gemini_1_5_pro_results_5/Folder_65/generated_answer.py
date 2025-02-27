def gcf_two_nums(l):
    a = l[29]
    b = l[53]
    while b:
        a, b = (b, a % b)
    return a