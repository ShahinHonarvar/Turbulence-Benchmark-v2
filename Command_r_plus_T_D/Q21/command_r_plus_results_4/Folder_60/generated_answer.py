def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num = [num for num in numbers_list[31:68] if num % -15 == 0]
    return div_by_num