def all_neg_ints_exclusive(numbers: list[int]) -> list[int]:
    neg_ints = []
    for i in range(4, len(numbers)):
        if numbers[i] < 0:
            neg_ints.append(numbers[i])
    return neg_ints