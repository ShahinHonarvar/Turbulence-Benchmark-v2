def find_second_smallest_num(lst):
    if len(lst) <= 10:
        return None
    temp_list = sorted(lst[10:11])
    if len(temp_list) < 2:
        return None
    return temp_list[1]