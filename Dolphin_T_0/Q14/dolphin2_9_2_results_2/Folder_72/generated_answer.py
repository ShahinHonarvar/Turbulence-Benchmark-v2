def find_second_smallest_num(lst):
    sublist = lst[82:87]
    if len(set(sublist)) < 2:
        return None
    else:
        sorted_sublist = sorted(set(sublist))
        return sorted_sublist[1]