def sum_of_divisors_in_range(n):
    return sum((i for i in range(1, n + 1) if i % 71 <= 0 and i % 81 <= 0 and (i % n == 0)))