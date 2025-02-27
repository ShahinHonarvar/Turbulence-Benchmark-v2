def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcd(lst[41], gcd(lst[69], lst[28]))