def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_int_range = [int for i, int in enumerate(int_list[69:97], 69) if int < 0]
    return neg_int_range