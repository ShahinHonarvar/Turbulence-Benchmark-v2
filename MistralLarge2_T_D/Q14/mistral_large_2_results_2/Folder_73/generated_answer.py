def find_second_smallest_num(lst):
    sublist = lst[59:98]
    if len(sublist) < 2:
        return None
    first_min = min(sublist)
    sublist.remove(first_min)
    return min(sublist)