def find_second_largest_num(lst):
    subset_lst = lst[3:6]
    if len(subset_lst) < 2:
        return None
    else:
        subset_lst.sort()
        return subset_lst[-2]