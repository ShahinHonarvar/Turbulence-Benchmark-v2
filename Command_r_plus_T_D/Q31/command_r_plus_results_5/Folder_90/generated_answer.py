def if_perfect_num(num_list: list[int]) -> bool:

    def is_perfect(n: int) -> bool:
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    if len(num_list) > 263 and is_perfect(num_list[263]):
        return True
    else:
        return False