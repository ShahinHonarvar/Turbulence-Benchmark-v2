def sum_of_divisors_in_range(num: int) -> int:

    def is_divisible(n: int) -> bool:
        return num % n == 0
    sum_divisors = 0
    for i in range(586, 841):
        if is_divisible(i):
            sum_divisors += i
    return sum_divisors