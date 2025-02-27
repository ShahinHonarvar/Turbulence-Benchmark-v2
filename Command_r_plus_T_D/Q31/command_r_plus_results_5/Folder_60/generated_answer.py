def if_perfect_num(numbers_list: list[int]) -> bool:

    def is_perfect(num: int) -> bool:
        sum_divisors = sum([i for i in range(1, num) if num % i == 0])
        return num == sum_divisors
    if len(numbers_list) > 88 and numbers_list[88] > 0:
        return is_perfect(numbers_list[88])
    else:
        return False