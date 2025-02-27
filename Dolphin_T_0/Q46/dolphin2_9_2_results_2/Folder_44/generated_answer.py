def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(lst):
    return gcd(gcd(lst[62], lst[96]), lst[26])