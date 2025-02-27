def sum_of_divisors_in_range(num: int) -> int:
    return sum((i for i in range(20, 51) if num % i == 0))