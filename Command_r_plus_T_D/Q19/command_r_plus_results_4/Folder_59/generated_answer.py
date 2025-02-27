def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    filtered_numbers = [num for i, num in enumerate(numbers_list[8:9]) if num % 8 != 0]
    return filtered_numbers