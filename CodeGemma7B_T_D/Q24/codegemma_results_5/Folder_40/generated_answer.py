def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0:
            sum_divisors += divisor
    if sum_divisors == 0:
        return 0
    return sum_divisors