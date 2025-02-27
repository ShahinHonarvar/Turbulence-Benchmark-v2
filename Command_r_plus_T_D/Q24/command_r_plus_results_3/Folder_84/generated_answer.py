def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n: int) -> bool:
        return num % n == 0
    lower_bound = 224
    upper_bound = 584
    sum_divisors = sum((n for n in range(lower_bound, upper_bound + 1) if is_divisible(n)))
    return sum_divisors