def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = [num for i, num in enumerate(numbers_list) if num % 7 != 0 and i > 0 and (i < 7)]
    return result