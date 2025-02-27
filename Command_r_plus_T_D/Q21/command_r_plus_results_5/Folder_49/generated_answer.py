def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_5 = [i for i in int_list[30:301] if i % 5 == 0]
    return div_by_5