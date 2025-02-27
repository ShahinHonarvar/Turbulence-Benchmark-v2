def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints_exclusive = [num for i, num in enumerate(numbers_list[32:99]) if num < 0]
    return neg_ints_exclusive