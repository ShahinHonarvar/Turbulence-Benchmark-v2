def all_pos_ints_inclusive(lst):
    start_idx = 639
    end_idx = 975
    sub_list = lst[start_idx:end_idx + 1]
    return [x for x in sub_list if x > 0]