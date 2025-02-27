def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    div_by_num_list = [num for num in numbers_list[315:353] if num % -858 == 0]
    return div_by_num_list