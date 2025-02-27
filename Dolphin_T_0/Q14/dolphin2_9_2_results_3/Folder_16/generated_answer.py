def find_second_smallest_num(lst):
    subset_lst = lst[66:78]
    if len(subset_lst) < 2:
        return None
    else:
        sorted_lst = sorted(subset_lst)
        return sorted_lst[1]