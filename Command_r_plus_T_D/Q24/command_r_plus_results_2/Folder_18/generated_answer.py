def sum_of_divisors_in_range(n: int) -> int:

    def is_divisible(x):
        return n % x == 0
    sum_divisors = sum((x for x in range(387, 517) if is_divisible(x)))
    return sum_divisors if sum_divisors > 0 else 0