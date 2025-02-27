def gcd(a, b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b

def gcf_two_nums(l):
    return gcd(l[25], l[80])