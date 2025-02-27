def find_second_smallest_num(lst):
    if len(lst) < 50:
        return None
    sliced_list = lst[35:50]
    if len(sliced_list) < 2:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]