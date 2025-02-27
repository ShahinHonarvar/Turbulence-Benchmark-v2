def find_second_largest_num(lst):
    sublist = lst[31:73]
    if len(sublist) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    if len(sublist) < 2:
        return None
    return max(sublist)