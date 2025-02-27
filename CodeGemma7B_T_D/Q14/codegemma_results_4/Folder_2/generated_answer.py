def find_second_smallest_num(lst):
    if len(lst) < 44 or len(lst) > 86:
        pass
    else:
        return sorted(lst[43:87])[1]