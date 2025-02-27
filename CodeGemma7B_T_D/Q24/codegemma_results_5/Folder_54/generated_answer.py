def sum_of_divisors_in_range(number):
    divisor = 36
    sum_of_divisors = 0
    while divisor <= 93:
        if number % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    return sum_of_divisors or 0