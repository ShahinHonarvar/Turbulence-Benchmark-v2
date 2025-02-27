def gcf_two_nums(l):
    a, b = (l[29], l[53])
    while b:
        a, b = (b, a % b)
    return a