import math

def gcf_three_nums(numbers):
    a = numbers[70]
    b = numbers[41]
    c = numbers[20]
    factors_a = find_factors(a)
    factors_b = find_factors(b)
    factors_c = find_factors(c)
    common_factors = factors_a & factors_b & factors_c
    return max(common_factors)

def find_factors(num):
    factors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return factors