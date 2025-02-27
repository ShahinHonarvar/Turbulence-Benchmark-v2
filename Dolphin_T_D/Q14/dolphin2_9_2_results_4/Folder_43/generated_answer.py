def find_second_smallest_num(lst):
    sublist = lst[74:96]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    second_smallest = sorted_sublist[1]
    if second_smallest == sorted_sublist[0]:
        return None
    return second_smallest