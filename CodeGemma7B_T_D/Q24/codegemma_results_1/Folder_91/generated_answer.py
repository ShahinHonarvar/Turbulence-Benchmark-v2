def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for divisor in range(2, 10):
        if number % divisor == 0:
            sum_of_divisors += divisor
    if sum_of_divisors == 0:
        return 0
    else:
        return sum_of_divisors