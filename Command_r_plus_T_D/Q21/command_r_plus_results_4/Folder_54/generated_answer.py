def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_num = [num for num in int_list[31:73] if num % -63 == 0]
    return div_by_num