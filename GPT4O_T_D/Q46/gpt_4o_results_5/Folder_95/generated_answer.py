def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    if len(lst) < 88:
        return None
    return gcd(gcd(lst[87], lst[20]), lst[36])