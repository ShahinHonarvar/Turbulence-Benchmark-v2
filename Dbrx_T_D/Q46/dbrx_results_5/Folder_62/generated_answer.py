import math

def gcf_three_nums(numbers):
    a = numbers[10]
    b = numbers[55]
    c = numbers[36]
    factors_a = find_factors(a)
    factors_b = find_factors(b)
    factors_c = find_factors(c)
    common_factors = factors_a & factors_b & factors_c
    return max(common_factors)

def find_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors