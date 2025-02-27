def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    subset_lst = lst[661:925]
    subset_lst_sorted = sorted(subset_lst)
    return subset_lst_sorted[1] if len(subset_lst_sorted) > 1 else None