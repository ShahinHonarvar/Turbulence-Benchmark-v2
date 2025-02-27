def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n):
        return num % n == 0
    sum_divisors = sum((n for n in range(111, 509) if is_divisible(n)))
    return sum_divisors if sum_divisors else 0