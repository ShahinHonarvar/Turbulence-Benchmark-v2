def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_69 = [num for i, num in enumerate(numbers_list[21:69]) if num % -69 != 0]
    return not_divisible_by_69