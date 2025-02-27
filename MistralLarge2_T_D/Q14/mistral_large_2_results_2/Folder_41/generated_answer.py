def find_second_smallest_num(lst):
    if len(lst) > 4:
        sub_list = sorted(lst[4:5])
        if len(sub_list) > 1:
            return sub_list[1]
    return None