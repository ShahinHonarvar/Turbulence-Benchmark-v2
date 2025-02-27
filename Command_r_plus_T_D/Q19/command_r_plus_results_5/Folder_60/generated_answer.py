def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    filtered_numbers = [num for i, num in enumerate(numbers_list) if num % -99 != 0 and 63 <= i < 73]
    return filtered_numbers