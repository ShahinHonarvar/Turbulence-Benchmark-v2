def find_second_largest_num(lst):
    slice_lst = lst[533:606]
    if len(slice_lst) < 2:
        return None
    max_num = max(slice_lst)
    second_max_num = max((i for i in slice_lst if i != max_num))
    return second_max_num