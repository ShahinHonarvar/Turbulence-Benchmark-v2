def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_six = [num for num in numbers_list[5:7] if num % -6 == 0]
    return div_by_six