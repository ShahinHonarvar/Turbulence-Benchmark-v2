def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = [num for num in numbers_list[0:4] if num % 8 != 0]
    return result