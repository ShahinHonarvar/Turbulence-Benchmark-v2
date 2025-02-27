def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_integers = [num for i, num in enumerate(numbers[20:43]) if num < 0]
    return neg_integers