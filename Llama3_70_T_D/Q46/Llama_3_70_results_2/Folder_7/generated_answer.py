def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    return gcd(gcd(lst[477], lst[696]), lst[663])