def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list[36:85]) if num % -27 != 0]