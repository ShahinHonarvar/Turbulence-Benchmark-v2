from functools import reduce
from math import gcd

def gcf_three_nums(numbers):
    operand1 = numbers[8]
    operand2 = numbers[2]
    operand3 = numbers[1]
    greatest_factor = reduce(gcd, [operand1, operand2, operand3])
    return greatest_factor