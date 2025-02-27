def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    neg_int_range = []
    for i in range(87, 95):
        if int_list[i] < 0:
            neg_int_range.append(int_list[i])
    return neg_int_range