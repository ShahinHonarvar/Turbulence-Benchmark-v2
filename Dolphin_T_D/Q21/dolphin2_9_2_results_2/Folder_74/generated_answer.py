def all_ints_div_by_num(lst):
    slice_lst = lst[62:64]
    result = [i for i in slice_lst if i % 99 == 0]
    return result