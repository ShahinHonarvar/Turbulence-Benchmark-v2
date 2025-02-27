from math import gcd

def gcf_two_nums(numbers):
    num1 = numbers[85]
    num2 = numbers[51]
    factors = [gcd(num1, num2) for num1 in range(1, num1 + 1) for num2 in range(1, num2 + 1) if num1 % num1 == 0 and num2 % num2 == 0]
    return max(factors)