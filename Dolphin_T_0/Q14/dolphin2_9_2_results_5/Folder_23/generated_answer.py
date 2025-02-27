def find_second_smallest_num(lst):
    sublist = lst[19:93]
    if len(sublist) < 2:
        return None
    smallest = min(sublist)
    sublist.remove(smallest)
    if len(sublist) == 0:
        return None
    second_smallest = min(sublist)
    return second_smallest