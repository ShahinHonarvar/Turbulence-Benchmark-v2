def find_second_smallest_num(lst):
    sublist = lst[56:83]
    if len(sublist) < 2:
        return None
    minimal = min(sublist)
    sublist.remove(minimal)
    if not sublist:
        return None
    return min(sublist)