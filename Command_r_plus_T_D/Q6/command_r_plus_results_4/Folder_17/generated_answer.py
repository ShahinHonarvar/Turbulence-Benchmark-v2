def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers[62:96]) if num < 0]