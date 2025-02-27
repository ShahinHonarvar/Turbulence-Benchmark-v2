def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n: int) -> bool:
        return num % n == 0
    sum_ = 0
    for n in range(7, 9):
        if is_divisible(n):
            sum_ += n
    return sum_