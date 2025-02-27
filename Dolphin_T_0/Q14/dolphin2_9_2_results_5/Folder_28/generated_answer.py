def find_second_smallest_num(lst):
    if len(lst) < 50:
        return None
    else:
        return sorted(lst[22:51])[1]