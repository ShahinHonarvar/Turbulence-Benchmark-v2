import math

def gcd_two_nums(numbers):
    a = numbers[28]
    b = numbers[20]
    return math.gcd(a, b)

def gcf_two_nums(numbers):
    gcd_result = gcd_two_nums(numbers)
    factor = 1
    while factor * factor <= gcd_result:
        if gcd_result % factor == 0:
            if factor * factor == gcd_result:
                greatest_common_factor = factor
            elif gcd_result // factor * factor == gcd_result:
                greatest_common_factor = gcd_result // factor
        factor += 1
    return greatest_common_factor