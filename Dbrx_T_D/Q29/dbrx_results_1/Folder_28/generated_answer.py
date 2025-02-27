import math

def gcf_two_nums(numbers):
    num1 = numbers[48]
    num2 = numbers[76]
    gcd_val = math.gcd(num1, num2)
    factor_list = [i for i in range(1, gcd_val + 1) if gcd_val % i == 0]
    return max(factor_list)