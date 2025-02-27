def find_second_smallest_num(lst):
    sub_list = lst[70:85]
    sorted_sub_list = sorted(sub_list)
    if len(sorted_sub_list) < 2:
        return 'None'
    else:
        return sorted_sub_list[1]