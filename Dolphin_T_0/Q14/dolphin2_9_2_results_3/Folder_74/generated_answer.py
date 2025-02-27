def find_second_smallest_num(lst):
    if len(lst) < 46:
        return None
    sublist = lst[35:47]
    if len(set(sublist)) < 2:
        return None
    else:
        return sorted(sublist)[1]