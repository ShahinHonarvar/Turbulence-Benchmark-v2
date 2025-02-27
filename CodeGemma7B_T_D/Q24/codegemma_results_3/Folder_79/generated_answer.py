def sum_of_divisors_in_range(num):
    sum = 0
    for divisor in range(1, 9):
        if num % divisor == 0:
            sum += divisor
    return sum