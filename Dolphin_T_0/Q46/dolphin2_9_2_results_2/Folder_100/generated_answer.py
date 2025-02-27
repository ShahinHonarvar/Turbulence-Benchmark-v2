def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(lst):
    a = lst[21]
    b = lst[51]
    c = lst[33]
    gcd_ab = gcd(a, b)
    gcf = gcd(gcd_ab, c)
    return gcf