def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_22_list = [num for num in numbers_list[43:60] if num % 22 == 0]
    return div_by_22_list