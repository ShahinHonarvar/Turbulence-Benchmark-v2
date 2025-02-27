def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def gcf_three_nums(lst):
    return gcd(gcd(lst[74], lst[51]), lst[27])