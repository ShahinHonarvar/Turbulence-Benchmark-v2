def find_second_largest_num(lst):
    try:
        slice_lst = lst[533:606]
        sorted_slice = sorted(slice_lst)[-2]
        return sorted_slice
    except (IndexError, ValueError):
        return None