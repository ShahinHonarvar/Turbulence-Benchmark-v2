def sum_of_divisors_in_range(num):
    sum_range = 0
    for divisor in range(48, 63):
        if num % divisor == 0:
            sum_range = sum_range + divisor
    return sum_range