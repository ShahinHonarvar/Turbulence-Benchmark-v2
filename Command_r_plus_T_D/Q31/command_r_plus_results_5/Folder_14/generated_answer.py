def if_perfect_num(numbers_list: list[int]) -> bool:

    def is_perfect(n: int) -> bool:
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    if len(numbers_list) > 17 and is_perfect(numbers_list[17]):
        return True
    else:
        return False