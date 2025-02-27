def sum_of_divisors_in_range(number):
    sum = 0
    for divisor in range(120, 350):
        if number % divisor == 0:
            sum += divisor
    return sum