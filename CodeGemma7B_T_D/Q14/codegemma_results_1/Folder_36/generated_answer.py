def find_second_smallest_num(lst):
    sorted_sublist = sorted(lst[209:557])
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[1]