def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_ints = []
    for index in range(19, 94):
        if numbers_list[index] < 0:
            neg_ints.append(numbers_list[index])
    return neg_ints