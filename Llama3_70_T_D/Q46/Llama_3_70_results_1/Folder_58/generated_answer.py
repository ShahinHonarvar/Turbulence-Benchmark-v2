def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcd(gcd(lst[145], lst[183]), lst[770])