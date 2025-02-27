def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(lst):
    return gcd(lst[31], gcd(lst[69], lst[40]))