def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n: int) -> bool:
        return num % n == 0
    divisors_sum = 0
    for n in range(16, 69):
        if is_divisible(n):
            divisors_sum += n
    return divisors_sum