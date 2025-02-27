def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_three_nums(lst):
    return gcd(gcd(lst[34], lst[38]), lst[77])