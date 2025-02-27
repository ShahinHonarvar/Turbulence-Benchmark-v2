def find_second_smallest_num(lst):
    sublist = lst[28:32]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]