def find_second_smallest_num(left_right_list):
    sublist = left_right_list[24:60]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    if len(sublist) < 1:
        return None
    second_min_num = min(sublist)
    return second_min_num