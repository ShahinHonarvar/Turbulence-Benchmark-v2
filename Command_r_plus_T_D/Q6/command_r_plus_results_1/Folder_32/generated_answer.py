def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_int_range = int_list[11:76]
    neg_ints = [num for num in neg_int_range if num < 0]
    return neg_ints