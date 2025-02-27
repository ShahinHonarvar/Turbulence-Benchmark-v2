def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_integers = []
    for i in range(43, 100):
        if numbers_list[i] < 0:
            neg_integers.append(numbers_list[i])
    return neg_integers