def find_second_smallest_num(lst):
    if len(lst) < 33:
        return None
    else:
        return sorted(lst[28:33])[1]