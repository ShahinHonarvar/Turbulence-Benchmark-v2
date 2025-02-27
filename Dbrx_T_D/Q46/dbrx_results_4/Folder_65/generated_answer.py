import math

def gcf_three_nums(numbers):
    a = numbers[18]
    b = numbers[10]
    c = numbers[76]
    factor = 1
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            factor = i
    gcf = factor
    return gcf