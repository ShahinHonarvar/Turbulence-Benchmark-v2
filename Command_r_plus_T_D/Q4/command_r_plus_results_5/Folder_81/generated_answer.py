def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    pos_ints = [int for i, int in enumerate(int_list, 10) if int > 0]
    return pos_ints[0:90] if len(pos_ints) > 90 else pos_ints