def find_second_smallest_num(lst):
    sliced_list = lst[60:201]
    if len(sliced_list) < 2:
        return None
    smallest = min(sliced_list)
    sliced_list.remove(smallest)
    return min(sliced_list)