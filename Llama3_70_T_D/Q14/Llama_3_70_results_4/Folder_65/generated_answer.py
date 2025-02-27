def find_second_smallest_num(lst):
    slice_of_lst = lst[56:58]
    sorted_lst = sorted(slice_of_lst)
    return sorted_lst[1] if len(sorted_lst) > 1 else None