def find_second_largest_num(lst):
    sublist = lst[28:41]
    if len(sublist) < 2:
        return None
    else:
        first_max = max(sublist)
        sublist.remove(first_max)
        return max(sublist) if sublist else None