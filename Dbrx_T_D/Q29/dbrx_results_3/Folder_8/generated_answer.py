import math

def gcf_two_nums(numbers):
    num1 = numbers[69]
    num2 = numbers[41]
    factor = int(math.sqrt(max(num1, num2)))
    while factor >= 1:
        if num1 % factor == 0 and num2 % factor == 0:
            return factor
        factor -= 1