def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    filtered_numbers = [num for i, num in enumerate(numbers_list) if num % 8 != 0 and i < 4]
    return filtered_numbers