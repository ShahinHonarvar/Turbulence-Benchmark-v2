def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    start_index = 598
    end_index = 767
    neg_int_range = []
    for i in range(start_index, end_index):
        if int_list[i] < 0:
            neg_int_range.append(int_list[i])
    return neg_int_range