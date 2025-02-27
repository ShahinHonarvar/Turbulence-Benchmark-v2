def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    filtered_numbers = [num for i, num in enumerate(numbers_list) if num % -61 and 86 <= i < 89]
    return filtered_numbers