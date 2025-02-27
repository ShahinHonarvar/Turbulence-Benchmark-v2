def sum_of_divisors_in_range(num):
    sum = 0
    for div in range(num):
        if num % div == 0 and div >= 3 and (div <= 7):
            sum += div
    return sum