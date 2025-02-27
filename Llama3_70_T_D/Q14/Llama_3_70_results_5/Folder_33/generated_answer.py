def find_second_smallest_num(lst):
    sliced_lst = lst[262:747]
    if len(sliced_lst) < 2:
        return None
    sorted_lst = sorted(sliced_lst)
    return sorted_lst[1]