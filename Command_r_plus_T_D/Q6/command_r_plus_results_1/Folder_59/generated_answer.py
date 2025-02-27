def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list) if num < 0 and 0 <= i < 9]