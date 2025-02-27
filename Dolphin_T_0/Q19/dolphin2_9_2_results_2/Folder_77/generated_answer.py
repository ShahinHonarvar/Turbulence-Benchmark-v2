def all_ints_not_div_by_num(lst, num=-172, start_index=668, end_index=739):
    return [i for i in lst[start_index:end_index] if i % num != 0]