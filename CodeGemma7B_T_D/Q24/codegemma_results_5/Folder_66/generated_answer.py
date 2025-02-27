def sum_of_divisors_in_range(num):
    sum_divisors = 0
    for factor in range(32, 36):
        if num % factor == 0:
            sum_divisors += factor
    return sum_divisors