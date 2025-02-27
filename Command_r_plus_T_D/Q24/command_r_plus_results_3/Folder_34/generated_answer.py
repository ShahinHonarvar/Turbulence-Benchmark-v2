def sum_of_divisors_in_range(num: int) -> int:
    if num <= 0:
        return 0
    divisors = [i for i in range(4, 6) if num % i == 0]
    return sum(divisors) if divisors else 0