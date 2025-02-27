def sum_of_divisors_in_range(n: int) -> int:
    return sum((i for i in range(3, 6) if n % i == 0))