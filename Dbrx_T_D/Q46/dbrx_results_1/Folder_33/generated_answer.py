import math

def gcf_three_nums(numbers):
    a, b, c = (numbers[252], numbers[149], numbers[564])
    divisor_range = range(1, min(a, b, c) + 1)[::-1]
    for num in divisor_range:
        if a % num == b % num == c % num == 0:
            return num