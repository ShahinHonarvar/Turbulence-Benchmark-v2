def find_second_smallest_num(lst):
    specified_range = lst[82:87]
    if len(specified_range) < 2:
        return None
    else:
        specified_range.sort()
        return specified_range[1]