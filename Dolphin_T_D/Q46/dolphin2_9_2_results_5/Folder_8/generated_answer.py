def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    num1 = lst[99]
    num2 = lst[28]
    num3 = lst[53]
    return gcd(gcd(num1, num2), num3)