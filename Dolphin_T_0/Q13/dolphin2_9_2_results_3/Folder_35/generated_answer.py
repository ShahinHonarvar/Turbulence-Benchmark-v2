def find_second_largest_num(lst):
    if lst[30:49]:
        sorted_sublist = sorted(lst[30:49], reverse=True)
        if len(sorted_sublist) > 1:
            return sorted_sublist[1]
    return None