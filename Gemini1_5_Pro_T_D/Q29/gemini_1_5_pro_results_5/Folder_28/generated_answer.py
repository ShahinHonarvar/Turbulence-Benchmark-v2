def gcf_two_nums(l):
    a = l[48]
    b = l[76]
    while b:
        a, b = (b, a % b)
    return a