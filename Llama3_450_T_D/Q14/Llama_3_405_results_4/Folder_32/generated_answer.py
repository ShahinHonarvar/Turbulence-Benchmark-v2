def find_second_smallest_num(lst):
    if len(lst) < 35:
        return None
    sliced_list = lst[32:36]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]