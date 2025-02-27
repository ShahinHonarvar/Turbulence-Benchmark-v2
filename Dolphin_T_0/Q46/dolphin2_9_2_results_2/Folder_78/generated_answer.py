def gcf_three_nums(lst):
    gcf = lst[13]
    for i in [lst[70], lst[32]]:
        gcf = gcd(gcf, i)
    return gcf

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return abs(a)