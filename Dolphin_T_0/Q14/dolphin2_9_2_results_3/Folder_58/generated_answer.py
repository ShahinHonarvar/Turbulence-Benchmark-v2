def find_second_smallest_num(lst):
    if len(lst) < 370:
        return None
    subset_lst = lst[310:371]
    if len(subset_lst) < 2:
        return None
    subset_lst.sort()
    return subset_lst[1]