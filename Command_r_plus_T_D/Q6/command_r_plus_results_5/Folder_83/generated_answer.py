def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints = [num for i, num in enumerate(int_list) if i >= 90 and i < 200 and (num < 0)]
    return neg_ints