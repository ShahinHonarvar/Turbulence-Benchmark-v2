def find_second_largest_num(lst):
    sub_list = lst[82:87]
    sub_list_sorted = sorted(set(sub_list))
    if len(sub_list_sorted) < 2:
        return None
    else:
        return sub_list_sorted[-2]