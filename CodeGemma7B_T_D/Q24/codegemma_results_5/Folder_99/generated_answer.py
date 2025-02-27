def sum_of_divisors_in_range(n):
    sum_of_divisors = 0
    for divisor in range(378, 783):
        if n % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors