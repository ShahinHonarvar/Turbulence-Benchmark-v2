def find_second_smallest_num(lst):
    sublist = lst[75:86]
    if len(sublist) < 2:
        return None
    else:
        return sorted(sublist)[1]