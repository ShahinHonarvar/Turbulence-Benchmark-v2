def all_ints_not_div_by_num(lst, start_index, end_index):
    return [i for i in lst[start_index:end_index] if i % 5 != 0]