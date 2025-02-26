def sum_of_divisors_in_range(n):
    range_sum = 0
    for i in range(228, 847):
        if n % i == 0:
            range_sum += i
    return range_sum