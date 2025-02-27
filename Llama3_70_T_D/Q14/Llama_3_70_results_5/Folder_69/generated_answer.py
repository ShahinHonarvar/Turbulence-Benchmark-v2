def find_second_smallest_num(lst):
    sliced_list = lst[25:88]
    if len(sliced_list) < 2:
        return None
    return sorted(sliced_list)[1]