def find_second_largest_num(lst):
    sublist = lst[20:201]
    if len(sublist) < 2:
        return None
    else:
        max_val = max(sublist)
        sublist.remove(max_val)
        if len(sublist) < 1:
            return None
        else:
            return max(sublist)