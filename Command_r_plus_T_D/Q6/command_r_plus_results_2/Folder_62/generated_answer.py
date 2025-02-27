def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_int_range = []
    for i in range(55, 84):
        if numbers_list[i] < 0:
            neg_int_range.append(numbers_list[i])
    return neg_int_range