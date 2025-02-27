def find_second_smallest_num(lst):
    subset_lst = lst[1:9]
    subset_lst.sort()
    if len(subset_lst) < 2:
        return None
    else:
        return subset_lst[1]