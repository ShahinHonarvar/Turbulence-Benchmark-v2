def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_ints = [num for i, num in enumerate(numbers[:6]) if num < 0]
    return neg_ints