def sum_of_divisors_in_range(num):
    total = 0
    for positive_factor in range(1, num + 1):
        if num % positive_factor == 0 and 0 < positive_factor <= 7:
            total += positive_factor
    return total