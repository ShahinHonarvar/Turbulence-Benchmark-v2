def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    return [num for num in numbers_list[60:200] if num % 9 != 0]