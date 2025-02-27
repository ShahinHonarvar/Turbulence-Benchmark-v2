def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_integers = [num for i, num in enumerate(numbers_list[10:76]) if num < 0]
    return neg_integers