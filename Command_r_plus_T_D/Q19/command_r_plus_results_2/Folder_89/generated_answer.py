def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list[48:62]) if num % 28 != 0]