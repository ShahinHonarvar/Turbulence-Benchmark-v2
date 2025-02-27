def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n):
        return num % n == 0
    if is_divisible(6):
        return 6
    elif is_divisible(7):
        return 7
    else:
        return 0