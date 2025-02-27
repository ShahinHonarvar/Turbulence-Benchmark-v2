def gcf_two_nums(l):
    a = l[129]
    b = l[582]
    while b:
        a, b = (b, a % b)
    return a