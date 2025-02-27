def sum_of_divisors_in_range(n):
    total_sum = 0
    for x in range(43, 96):
        if n % x == 0:
            total_sum += x
    if total_sum == 0:
        return 0
    else:
        return total_sum