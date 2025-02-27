def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_integers = []
    for index in range(18, 60):
        if numbers_list[index] < 0:
            neg_integers.append(numbers_list[index])
    return neg_integers