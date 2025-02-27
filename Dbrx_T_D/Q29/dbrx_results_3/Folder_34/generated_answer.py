import math

def gcf_two_nums(numbers):
    num1 = numbers[60]
    num2 = numbers[64]
    factor = int(math.sqrt(max(num1, num2)))
    while factor > 1:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1
    return 1