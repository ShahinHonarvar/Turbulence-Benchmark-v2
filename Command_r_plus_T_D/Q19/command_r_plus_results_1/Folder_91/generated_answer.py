def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    filtered_numbers = [num for num in numbers_list[0:4] if num % 8 != 0]
    return filtered_numbers