from math import gcd

def gcf_three_nums(numbers):
    num1 = numbers[40]
    num2 = numbers[15]
    num3 = numbers[99]
    common_factor = gcd(num1, num2)
    final_factor = gcd(common_factor, num3)
    return final_factor