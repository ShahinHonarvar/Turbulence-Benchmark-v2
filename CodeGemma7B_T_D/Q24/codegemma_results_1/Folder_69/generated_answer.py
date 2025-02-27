def sum_of_divisors_in_range(num):
    start, end = (658, 868)
    sum_divisors = 0
    for divisor in range(start, end + 1):
        if num % divisor == 0 and divisor in range(start, end + 1):
            sum_divisors += divisor
    return sum_divisors if sum_divisors != 0 else 0