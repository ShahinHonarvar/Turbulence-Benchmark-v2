def find_second_smallest_num(lst):
    if len(lst) < 60:
        return None
    else:
        return sorted(lst[25:60])[1]