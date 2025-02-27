def find_second_smallest_num(lst):
    sublist = lst[21:51]
    if len(sublist) < 2:
        return None
    else:
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]