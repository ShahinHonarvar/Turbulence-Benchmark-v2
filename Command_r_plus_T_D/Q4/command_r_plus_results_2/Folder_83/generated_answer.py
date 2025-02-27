def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list[90:200], 90) if num > 0]