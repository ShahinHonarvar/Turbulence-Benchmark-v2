def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(lst):
    return gcd(gcd(lst[20], lst[35]), lst[74])