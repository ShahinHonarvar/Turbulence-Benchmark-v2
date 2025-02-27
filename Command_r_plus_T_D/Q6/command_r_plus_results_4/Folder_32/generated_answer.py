def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints = [int for int in int_list[11:76] if int < 0]
    return neg_ints