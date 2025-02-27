def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_90 = [num for num in int_list[57:68] if num % 90 == 0]
    return div_by_90