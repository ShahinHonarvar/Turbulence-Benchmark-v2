def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_two_nums(lst):
    num1 = lst[47]
    num2 = lst[10]
    return gcd(num1, num2)