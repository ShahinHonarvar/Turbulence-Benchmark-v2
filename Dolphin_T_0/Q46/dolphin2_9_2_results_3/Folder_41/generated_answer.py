def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers_list):
    num1 = numbers_list[19]
    num2 = numbers_list[94]
    num3 = numbers_list[78]
    gcf = gcd(gcd(num1, num2), num3)
    return gcf