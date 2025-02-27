def find_second_smallest_num(lst):
    sublist = lst[55:99]
    if len(sublist) < 2:
        return None
    min1 = min(sublist)
    if min1 == max(sublist):
        return None
    sublist.remove(min1)
    min2 = min(sublist)
    return min2