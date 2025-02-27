def gcf_three_nums(l):
    a = l[99]
    b = l[63]
    c = l[74]
    i = min(a, b, c)
    while i > 1:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            return i
        i -= 1
    return 1