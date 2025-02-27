def sum_of_divisors_in_range(num):
    range_start = 41
    range_end = 55
    sum = 0
    for divisor in range(1, num + 1):
        if num % divisor == 0 and range_start <= divisor <= range_end:
            sum += divisor
    return sum or 0