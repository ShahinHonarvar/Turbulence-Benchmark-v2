def find_second_smallest_num(lst):
    if 62 < len(lst) and 63 < len(lst):
        sub_list = lst[62:64]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
    return None