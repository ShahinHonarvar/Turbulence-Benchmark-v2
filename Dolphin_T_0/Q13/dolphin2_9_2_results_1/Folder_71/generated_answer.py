def find_second_largest_num(lst):
    if 52 >= len(lst) >= 26:
        subset_lst = lst[26:53]
        if len(set(subset_lst)) < 2:
            return None
        subset_lst.sort()
        return subset_lst[-2]
    else:
        return None