def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints = [num for num in int_list[50:200] if num < 0]
    return neg_ints