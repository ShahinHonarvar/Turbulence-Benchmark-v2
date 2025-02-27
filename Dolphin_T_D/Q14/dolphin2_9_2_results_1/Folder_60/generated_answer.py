def find_second_smallest_num(lst):
    sublist = lst[56:99]
    if not sublist:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    if sublist:
        return min(sublist)
    else:
        return None