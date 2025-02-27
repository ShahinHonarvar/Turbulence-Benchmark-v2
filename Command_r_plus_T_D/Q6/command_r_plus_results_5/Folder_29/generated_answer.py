def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_integers = []
    for i in range(48, 76):
        if numbers[i] < 0:
            neg_integers.append(numbers[i])
    return neg_integers