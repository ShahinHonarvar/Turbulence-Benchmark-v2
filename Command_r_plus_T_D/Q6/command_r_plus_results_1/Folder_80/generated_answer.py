def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints_range = numbers_list[69:97]
    neg_ints = [num for num in neg_ints_range if num < 0]
    return neg_ints