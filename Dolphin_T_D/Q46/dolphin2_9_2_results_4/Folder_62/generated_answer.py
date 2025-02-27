def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(lst):
    num1 = lst[10]
    num2 = lst[55]
    num3 = lst[36]
    result = gcd(gcd(num1, num2), num3)
    return result