def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_integers = []
    for idx in range(19, 94):
        if numbers_list[idx] < 0:
            neg_integers.append(numbers_list[idx])
    return neg_integers