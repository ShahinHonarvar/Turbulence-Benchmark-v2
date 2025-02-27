def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_numbers = [num for i, num in enumerate(numbers_list[:7]) if num < 0]
    return neg_numbers