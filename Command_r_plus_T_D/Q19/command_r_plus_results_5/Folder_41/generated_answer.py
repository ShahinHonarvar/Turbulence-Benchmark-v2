def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    result = [num for i, num in enumerate(numbers_list) if num % -3 != 0 and 0 < i < 8]
    return result