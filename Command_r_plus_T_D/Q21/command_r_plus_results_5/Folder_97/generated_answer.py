def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_89 = [num for num in int_list[17:64] if num % 89 == 0]
    return div_by_89