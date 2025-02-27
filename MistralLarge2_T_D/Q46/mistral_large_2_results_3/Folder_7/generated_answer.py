def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    a = lst[477]
    b = lst[696]
    c = lst[663]
    return gcd(gcd(a, b), c)