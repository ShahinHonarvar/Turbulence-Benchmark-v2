def sum_of_divisors_in_range(number):
    sum = 0
    for divisor in range(7, 9):
        if number % divisor == 0:
            sum += divisor
    return sum or 0