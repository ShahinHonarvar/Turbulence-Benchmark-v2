def all_ints_div_by_num(lst, num=46, start_index=21, end_index=97):
    return [i for i in lst[start_index:end_index + 1] if i % num == 0]