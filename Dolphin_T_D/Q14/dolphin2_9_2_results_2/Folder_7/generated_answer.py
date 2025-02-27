def find_second_smallest_num(lst):
    sublist = lst[686:988]
    if len(sublist) < 2:
        return None
    smallest1 = min(sublist)
    sublist.remove(smallest1)
    smallest2 = min(sublist)
    return smallest2 if smallest2 != smallest1 else None