def sum_of_divisors_in_range(number):
    sum_of_divisors = 0
    for divisor in range(1, number + 1):
        if number % divisor == 0 and divisor >= 157 and (divisor <= 902):
            sum_of_divisors += divisor
    return sum_of_divisors