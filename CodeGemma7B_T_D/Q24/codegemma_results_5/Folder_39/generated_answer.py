def sum_of_divisors_in_range(num):
    sum_of_divisors = 0
    for divisor in range(11, 57):
        if num % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors