def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n):
        return num % n == 0
    sum_divisors = 0
    for n in range(228, 847):
        if is_divisible(n):
            sum_divisors += n
    return sum_divisors