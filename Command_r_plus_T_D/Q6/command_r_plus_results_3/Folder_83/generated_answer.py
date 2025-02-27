def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_ints_in_range = [num for i, num in enumerate(int_list[90:200]) if num < 0]
    return neg_ints_in_range