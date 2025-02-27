def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    return [num for i, num in enumerate(numbers[56:92], 56) if num < 0]