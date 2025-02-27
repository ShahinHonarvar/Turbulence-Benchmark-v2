def gcd(a, b):
    while b > 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(lst):
    return gcd(lst[43], lst[99])