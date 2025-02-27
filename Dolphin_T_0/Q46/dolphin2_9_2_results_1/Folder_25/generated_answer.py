def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_three_nums(lst):
    a = lst[32]
    b = lst[54]
    c = lst[13]
    return gcd(gcd(a, b), c)