def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers) if i >= 48 and i < 76 and (num < 0)]