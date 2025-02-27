def sum_of_divisors_in_range(n):
    if n < 27:
        return 0
    return sum((i for i in range(27, 45) if n % i == 0))