def all_neg_ints_exclusive(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[38:81], 38) if num < 0]