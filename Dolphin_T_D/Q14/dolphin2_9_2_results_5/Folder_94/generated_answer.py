def find_second_smallest_num(lst):
    sublist = lst[52:72]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    if len(sublist) < 1:
        return None
    return min(sublist)