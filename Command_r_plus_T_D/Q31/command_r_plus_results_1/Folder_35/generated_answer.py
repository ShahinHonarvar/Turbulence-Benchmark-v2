def if_perfect_num(numbers: list[int]) -> bool:

    def is_perfect(n: int) -> bool:
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    return is_perfect(numbers[993])