def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    slice_lst = lst[50:55]
    first_min = min(slice_lst)
    slice_lst.remove(first_min)
    second_min = min(slice_lst)
    return second_min if second_min != first_min else None