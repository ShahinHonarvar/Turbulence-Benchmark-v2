def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(lst):
    a = lst[16]
    b = lst[87]
    c = lst[95]
    return gcd(gcd(a, b), c)