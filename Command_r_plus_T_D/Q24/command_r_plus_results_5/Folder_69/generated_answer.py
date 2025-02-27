def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n: int) -> bool:
        return num % n == 0
    lower_bound = 658
    upper_bound = 868
    divisors_sum = sum((n for n in range(lower_bound, upper_bound + 1) if is_divisible(n)))
    return divisors_sum if divisors_sum > 0 else 0