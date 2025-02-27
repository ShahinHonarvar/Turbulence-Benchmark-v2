def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    positive_ints = [i for i in int_list[10:80] if i > 0]
    return positive_ints