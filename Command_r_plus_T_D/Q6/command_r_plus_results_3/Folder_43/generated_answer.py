def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_int_range = numbers_list[38:77]
    neg_ints = [num for num in neg_int_range if num < 0]
    return neg_ints