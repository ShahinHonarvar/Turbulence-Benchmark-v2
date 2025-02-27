def if_perfect_num(numbers_list: list[int]) -> bool:

    def check_perfect_number(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers_list) > 537 and numbers_list[537] > 0:
        return check_perfect_number(numbers_list[537])
    else:
        return False