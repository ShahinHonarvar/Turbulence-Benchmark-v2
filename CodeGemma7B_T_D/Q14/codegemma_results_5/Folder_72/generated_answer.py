def find_second_smallest_num(lst):
    if 82 <= min(lst[82:87]) <= 86:
        return sorted(lst[82:87])[1]
    else:
        return None