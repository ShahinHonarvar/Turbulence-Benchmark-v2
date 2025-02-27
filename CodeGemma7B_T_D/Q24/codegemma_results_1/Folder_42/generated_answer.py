def sum_of_divisors_in_range(n):
    result = 0
    for factor in range(14, 94):
        if n % factor == 0:
            result += factor
    return result or 0