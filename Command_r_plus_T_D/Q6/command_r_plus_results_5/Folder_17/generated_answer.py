def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_range = numbers_list[62:96]
    return [num for num in neg_range if num < 0]