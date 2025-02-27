def gcf_two_nums(l):
    a = l[860]
    b = l[307]
    while b:
        a, b = (b, a % b)
    return a