def find_second_largest_num(lst):
    if 98 >= 56 and len(lst) > 56 + 1:
        subset_lst = lst[56:99]
        if len(set(subset_lst)) >= 2:
            sorted_subset_lst = sorted(set(subset_lst), reverse=True)
            return sorted_subset_lst[1]
        else:
            return None
    else:
        return None