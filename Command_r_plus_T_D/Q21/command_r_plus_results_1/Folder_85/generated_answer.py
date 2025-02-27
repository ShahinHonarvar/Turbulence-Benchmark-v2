def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num_list = [num for num in numbers_list[6:9] if num % -9 == 0]
    return div_by_num_list