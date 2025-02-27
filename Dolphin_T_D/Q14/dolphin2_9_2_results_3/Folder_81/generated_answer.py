def find_second_smallest_num(lst):
    sub_list = lst[10:101]
    if len(sub_list) < 2:
        return None
    min_num = min(sub_list)
    second_min_num = min((val for val in sub_list if val != min_num))
    return second_min_num