def find_second_largest_num(lst):
    sliced_list = lst[34:56]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort(reverse=True)
    return sliced_list[1]