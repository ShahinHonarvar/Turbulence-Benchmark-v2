def find_second_largest_num(lst):
    subset_lst = lst[262:747]
    if len(subset_lst) < 2:
        return None
    else:
        first_max = max(subset_lst)
        subset_lst.remove(first_max)
        return max(subset_lst)