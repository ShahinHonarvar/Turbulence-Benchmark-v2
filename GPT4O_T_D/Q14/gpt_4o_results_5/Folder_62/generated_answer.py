def find_second_smallest_num(lst):
    sublist = lst[10:67]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]