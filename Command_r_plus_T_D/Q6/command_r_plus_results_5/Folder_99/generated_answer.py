def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers[295:573]) if num < 0]