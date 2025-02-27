def find_second_smallest_num(lst):
    if len(lst) < 52:
        return None
    else:
        return sorted(lst[37:52])[1]