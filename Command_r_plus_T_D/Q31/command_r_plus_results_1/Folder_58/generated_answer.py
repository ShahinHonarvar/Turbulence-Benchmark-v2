def if_perfect_num(num_list: list[int]) -> bool:

    def is_perfect(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    if len(num_list) > 714 and num_list[714] > 0:
        return is_perfect(num_list[714])
    else:
        return False