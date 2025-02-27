def all_ints_div_by_num(lst, num=885, start_idx=421, end_idx=489):
    return [val for val in lst[start_idx:end_idx + 1] if val % num == 0]