def find_second_smallest_num(lst):
    specified_range = lst[28:39]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[1]