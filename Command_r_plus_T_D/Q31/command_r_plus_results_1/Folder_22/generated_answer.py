def if_perfect_num(num_list: list[int]) -> bool:

    def check_perfect(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(num_list) > 72 and num_list[72] > 0:
        return check_perfect(num_list[72])
    else:
        return False