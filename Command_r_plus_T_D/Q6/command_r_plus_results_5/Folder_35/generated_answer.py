def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_int_range = int_list[10:80]
    return [num for num in neg_int_range if num < 0]