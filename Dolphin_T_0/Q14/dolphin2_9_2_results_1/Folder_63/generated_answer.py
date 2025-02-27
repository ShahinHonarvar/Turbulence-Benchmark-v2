def find_second_smallest_num(lst):
    if len(lst) == 0 or len(lst) < 82:
        return None
    else:
        sublist = lst[55:83]
        if len(set(sublist)) < 2:
            return None
        sorted_sublist = sorted(sublist)
        return sorted_sublist[1]