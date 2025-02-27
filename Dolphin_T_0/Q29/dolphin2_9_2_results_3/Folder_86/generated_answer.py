def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_two_nums(l):
    return gcd(l[793], l[449])