def find_second_smallest_num(lst):
    sublist = lst[60:201]
    if len(sublist) < 2:
        return None
    min_value = min(sublist)
    sublist.remove(min_value)
    if len(sublist) > 1:
        return min(sublist)
    else:
        return None