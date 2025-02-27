def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints = [num for i, num in enumerate(int_list[1:7]) if num < 0]
    return neg_ints