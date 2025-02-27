def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_99 = [num for num in int_list[62:64] if num % 99 == 0]
    return div_by_99