def sum_of_divisors_in_range(n):
    result = 0
    for divisor in range(4, 10):
        if n % divisor == 0:
            result += divisor
    if result == 0:
        return 0
    else:
        return result