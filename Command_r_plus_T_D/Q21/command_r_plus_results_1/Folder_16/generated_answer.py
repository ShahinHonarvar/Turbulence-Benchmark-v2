def all_ints_div_by_num(int_list: list[int]) -> list[int]:
    div_by_71 = [num for num in int_list[13:69] if num % 71 == 0]
    return div_by_71