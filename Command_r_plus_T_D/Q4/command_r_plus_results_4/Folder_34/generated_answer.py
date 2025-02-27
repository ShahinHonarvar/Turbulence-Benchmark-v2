def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    pos_ints = [num for num in int_list[60:200] if num > 0]
    return pos_ints