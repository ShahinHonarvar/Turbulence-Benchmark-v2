def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_28 = [num for num in numbers_list[36:41] if num % 28 == 0]
    return div_by_28