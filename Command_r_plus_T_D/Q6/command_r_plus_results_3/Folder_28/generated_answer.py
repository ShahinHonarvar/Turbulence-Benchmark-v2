def all_neg_ints_exclusive(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[20:51], 20) if num < 0]