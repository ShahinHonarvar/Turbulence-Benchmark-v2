def if_perfect_num(num_list: list[int]) -> bool:

    def is_perfect(n: int) -> bool:
        sum_divisors = sum([i for i in range(1, n) if n % i == 0])
        return sum_divisors == n
    if len(num_list) > 702 and num_list[702] > 0:
        return is_perfect(num_list[702])
    else:
        return False