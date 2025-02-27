def sum_of_divisors_in_range(n):
    result = 0
    for divisor in range(111, 509):
        if n % divisor == 0:
            result += divisor
    return result