def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    pos_ints = [int for int in int_list[10:80] if int > 0]
    return pos_ints