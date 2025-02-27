def all_ints_div_by_num(lst, start_index=10, end_index=52, num=-12):
    return [i for i in lst[start_index:end_index + 1] if i % num == 0]