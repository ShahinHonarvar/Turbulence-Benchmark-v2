def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num_list = [num for num in numbers_list[14:57] if num % -59 == 0]
    return div_by_num_list