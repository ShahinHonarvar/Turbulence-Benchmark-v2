def sum_of_divisors_in_range(n):
    if n <= 48:
        return 0
    return sum([i for i in range(48, 93) if n % i == 0])