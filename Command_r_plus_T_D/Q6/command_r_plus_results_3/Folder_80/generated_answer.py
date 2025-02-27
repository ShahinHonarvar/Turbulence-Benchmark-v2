def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers_list[69:97]) if num < 0]