def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_num = [int for int in int_list[572:807] if int % -158 == 0]
    return div_by_num