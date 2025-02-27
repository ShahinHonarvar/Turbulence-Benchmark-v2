import math

def gcf_two_nums(numbers):
    num1 = numbers[38]
    num2 = numbers[77]
    for i in range(2, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factor = i
    return common_factor