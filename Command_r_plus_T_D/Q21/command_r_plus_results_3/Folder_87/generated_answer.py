def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_16 = [num for num in numbers_list[10:57] if num % 16 == 0]
    return div_by_16