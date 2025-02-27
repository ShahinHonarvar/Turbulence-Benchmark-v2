def find_second_largest_num(lst):
    subset_lst = lst[43:52]
    if len(set(subset_lst)) < 2:
        return None
    else:
        sorted_lst = sorted(set(subset_lst), reverse=True)
        return sorted_lst[1]