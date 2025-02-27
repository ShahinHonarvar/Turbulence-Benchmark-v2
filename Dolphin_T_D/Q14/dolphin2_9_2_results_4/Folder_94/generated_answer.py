def find_second_smallest_num(lst):
    if len(lst) < 72:
        return None
    else:
        return sorted(lst[51:72])[1]