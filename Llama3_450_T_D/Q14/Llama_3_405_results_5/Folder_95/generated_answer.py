def find_second_smallest_num(lst):
    specified_slice = lst[75:86]
    if len(specified_slice) < 2:
        return None
    else:
        return sorted(specified_slice)[1]