def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints = []
    for i in range(2, 8):
        if numbers_list[i] < 0:
            neg_ints.append(numbers_list[i])
    return neg_ints