def find_second_largest_num(lst):
    if len(lst) < 201:
        return None
    sliced_list = lst[20:201]
    sorted_list = sorted(sliced_list, reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]