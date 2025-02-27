def find_second_smallest_num(lst):
    sliced_list = sorted(lst[26:53])
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]