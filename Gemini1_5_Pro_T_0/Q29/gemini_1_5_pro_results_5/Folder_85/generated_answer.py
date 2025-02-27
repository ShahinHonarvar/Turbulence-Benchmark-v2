def gcf_two_nums(l):
    a = l[38]
    b = l[77]
    while b:
        a, b = (b, a % b)
    return a