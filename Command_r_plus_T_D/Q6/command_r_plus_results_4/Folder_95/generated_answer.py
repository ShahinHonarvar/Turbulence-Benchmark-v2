def all_neg_ints_exclusive(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[25:80], 25) if num < 0]