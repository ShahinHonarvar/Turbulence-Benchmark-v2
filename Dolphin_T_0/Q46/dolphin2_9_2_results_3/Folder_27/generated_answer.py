def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcd(gcd(lst[76], lst[64]), lst[28])