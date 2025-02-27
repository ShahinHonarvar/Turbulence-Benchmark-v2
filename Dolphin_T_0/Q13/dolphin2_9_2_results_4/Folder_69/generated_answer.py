def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 35:
        return None
    sublist = lst[32:36]
    if len(set(sublist)) < 2:
        return None
    max_num = max(sublist)
    sublist.remove(max_num)
    return max(sublist)