def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcf_two_nums(lst):
    return gcd(lst[87], lst[95])