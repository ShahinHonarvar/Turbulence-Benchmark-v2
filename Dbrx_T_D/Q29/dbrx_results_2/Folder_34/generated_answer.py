import math

def gcf_two_nums(numbers):
    num1 = numbers[60]
    num2 = numbers[64]
    factor = int(math.sqrt(max(num1, num2)))
    gcf = 0
    for i in range(1, factor + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf