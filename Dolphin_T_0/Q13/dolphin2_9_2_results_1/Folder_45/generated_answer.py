def find_second_largest_num(lst):
    if not lst:
        return None
    else:
        slice_lst = lst[30:201]
        max_num = max(slice_lst)
        slice_lst.remove(max_num)
        if slice_lst:
            return max(slice_lst)
        else:
            return None