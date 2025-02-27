def sum_of_divisors_in_range(num: int) -> int:
    if num < 1:
        return 0
    divisors = [i for i in range(1, 3) if num % i == 0]
    return sum(divisors)