def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcd(gcd(lst[695], lst[710]), lst[914])