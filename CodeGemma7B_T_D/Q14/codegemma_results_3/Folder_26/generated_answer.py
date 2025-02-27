def find_second_smallest_num(lst):
    if not lst or len(lst) < 2:
        return None
    sorted_list = sorted(lst[62:79])
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]