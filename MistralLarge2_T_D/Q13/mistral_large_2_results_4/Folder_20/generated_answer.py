def find_second_largest_num(lst):
    sublist = lst[56:67]
    if len(sublist) < 2:
        return None
    first_max = max(sublist)
    sublist.remove(first_max)
    return max(sublist) if sublist else None