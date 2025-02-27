def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num = [num for num in numbers_list[75:89] if num % -27 == 0]
    return div_by_num