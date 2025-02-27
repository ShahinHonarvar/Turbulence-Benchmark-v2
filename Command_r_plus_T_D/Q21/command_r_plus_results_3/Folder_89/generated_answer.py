def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    result = [num for num in int_list[30:60] if num % 39 == 0]
    return result