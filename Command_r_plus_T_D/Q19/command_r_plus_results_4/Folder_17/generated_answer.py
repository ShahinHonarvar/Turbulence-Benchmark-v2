def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list) if num % 84 != 0 and 39 <= i < 57]