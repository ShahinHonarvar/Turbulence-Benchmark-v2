def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_integers = [num for i, num in enumerate(numbers[10:76]) if num < 0]
    return neg_integers