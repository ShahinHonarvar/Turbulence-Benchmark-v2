def sum_of_divisors_in_range(num):
    if num < 3:
        return 0
    sum_divisors = 0
    for divisor in range(3, 6):
        if num % divisor == 0:
            sum_divisors += divisor
    return sum_divisors