def find_second_largest_num(lst):
    if 28 <= 38 < len(lst):
        sub_list = lst[28:39]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[-2]
    return None