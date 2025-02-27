def sum_of_divisors_in_range(n):
    if n < 13 or n > 62:
        return 0
    sum_of_divisors = 0
    for divisor in range(13, 63):
        if n % divisor == 0:
            sum_of_divisors += divisor
    return sum_of_divisors