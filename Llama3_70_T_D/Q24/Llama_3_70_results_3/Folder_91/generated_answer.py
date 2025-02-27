def sum_of_divisors_in_range(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    return sum((i for i in range(2, 10) if n % i == 0))