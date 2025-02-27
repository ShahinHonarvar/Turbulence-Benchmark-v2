def sum_of_divisors_in_range(n):
    if n < 1:
        return 0
    total_sum = 0
    for i in range(83, 96):
        if n % i == 0:
            total_sum += i
    return total_sum