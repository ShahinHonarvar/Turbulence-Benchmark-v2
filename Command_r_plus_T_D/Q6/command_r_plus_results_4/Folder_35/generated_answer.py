def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints = [num for i, num in enumerate(int_list) if 10 <= i < 80 and num < 0]
    return neg_ints