def find_second_smallest_num(lst):
    if len(lst) <= 200 or 30 >= len(lst):
        sliced_list = lst[30:]
    else:
        sliced_list = lst[30:201]
    if len(sliced_list) < 2:
        return None
    return sorted(sliced_list)[1]