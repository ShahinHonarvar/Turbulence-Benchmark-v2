def all_neg_ints_exclusive(lst: list[int]) -> list[int]:
    return [num for i, num in enumerate(lst[10:80], start=10) if num < 0]