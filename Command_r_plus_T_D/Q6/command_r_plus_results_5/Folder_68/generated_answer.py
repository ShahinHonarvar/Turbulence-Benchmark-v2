def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_numbers = [num for i, num in enumerate(numbers) if num < 0 and i < 8]
    return neg_numbers