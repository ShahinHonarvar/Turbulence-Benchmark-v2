def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_100 = [num for i, num in enumerate(numbers_list) if num % 100 != 0 and 10 <= i < 100]
    return not_divisible_by_100