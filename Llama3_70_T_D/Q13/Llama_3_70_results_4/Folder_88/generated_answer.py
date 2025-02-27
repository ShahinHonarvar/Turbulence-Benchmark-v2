def find_second_largest_num(lst):
    if len(lst) < 9:
        return None
    else:
        slice_lst = lst[4:9]
        max_num = max(slice_lst)
        slice_lst.remove(max_num)
        if len(slice_lst) == 0:
            return None
        else:
            return max(slice_lst)