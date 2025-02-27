def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num_list = [num for num in numbers_list[10:83] if num % -47 == 0]
    return div_by_num_list