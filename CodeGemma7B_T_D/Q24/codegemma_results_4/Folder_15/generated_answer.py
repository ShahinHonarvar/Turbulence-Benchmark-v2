def sum_of_divisors_in_range(n):
    if n <= 6 or n >= 9:
        return 0
    return n + 6 + (n - 6)