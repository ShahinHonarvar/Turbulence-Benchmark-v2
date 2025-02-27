def find_second_largest_num(lst):
    sublist = lst[37:52] if 37 <= len(lst) <= 51 else None
    if sublist:
        max_num = max(sublist)
        sublist.remove(max_num)
        return max(sublist)
    else:
        return None