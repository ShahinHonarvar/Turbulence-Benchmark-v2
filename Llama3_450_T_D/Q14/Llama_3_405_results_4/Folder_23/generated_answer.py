def find_second_smallest_num(lst):
    if len(lst) < 92 or 19 > len(lst):
        return None
    sliced_list = lst[19:93]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]