def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list[30:301]) if num % 5 == 0]