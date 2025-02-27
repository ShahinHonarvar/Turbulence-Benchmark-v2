def find_second_smallest_num(lst):
    specified_slice = lst[22:51]
    if len(specified_slice) < 2:
        return None
    return sorted(specified_slice)[1]