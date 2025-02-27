def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_int_range = []
    for index, num in enumerate(numbers_list[7:9], start=7):
        if num < 0:
            neg_int_range.append(num)
    return neg_int_range