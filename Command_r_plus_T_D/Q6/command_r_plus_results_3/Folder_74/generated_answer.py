def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list[13:70], 13) if num < 0]