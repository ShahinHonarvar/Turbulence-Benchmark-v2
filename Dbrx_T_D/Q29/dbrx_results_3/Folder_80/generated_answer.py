import math

def gcf_two_nums(numbers):
    a = numbers[95]
    b = numbers[85]
    while b != 0:
        a, b = (b, a % b)
    return int(math.fabs(a))