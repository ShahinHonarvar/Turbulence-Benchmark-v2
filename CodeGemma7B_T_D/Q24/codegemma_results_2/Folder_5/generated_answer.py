def sum_of_divisors_in_range(num):
    divisor = 7
    sum_of_divisors = 0
    while divisor <= 8:
        if num % divisor == 0:
            sum_of_divisors += divisor
        divisor += 1
    return sum_of_divisors