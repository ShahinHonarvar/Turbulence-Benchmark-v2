def find_second_smallest_num(lst):
    sub_list = lst[20:31]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) > 1:
        return sorted_sub_list[1]
    else:
        return 'None'