def find_second_smallest_num(lst):
    sublist = lst[75:89]
    if len(sublist) < 2:
        return None
    min_num = min(sublist)
    sublist.remove(min_num)
    second_min_num = min(sublist)
    return second_min_num if second_min_num != None else second_min_num