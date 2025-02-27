def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers[20:43]) if num < 0]