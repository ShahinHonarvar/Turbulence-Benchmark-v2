def if_perfect_num(numbers_list: list[int]) -> bool:

    def check_perfect_num(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return sum_divisors == num
    if len(numbers_list) > 8 and numbers_list[8] > 0:
        return check_perfect_num(numbers_list[8])
    else:
        return False