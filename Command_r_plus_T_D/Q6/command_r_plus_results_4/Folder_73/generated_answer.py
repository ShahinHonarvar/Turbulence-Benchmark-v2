def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_integers = [num for i, num in enumerate(numbers[36:85]) if num < 0]
    return neg_integers