def sum_of_divisors_in_range(n):
    sum = 0
    for divisor in range(392, 466):
        if n % divisor == 0:
            sum += divisor
    return sum