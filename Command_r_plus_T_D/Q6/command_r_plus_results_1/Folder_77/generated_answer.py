def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints_range = []
    for i in range(111, 473):
        if numbers_list[i] < 0:
            neg_ints_range.append(numbers_list[i])
    return neg_ints_range