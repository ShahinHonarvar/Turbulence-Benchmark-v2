def find_second_smallest_num(lst):
    if len(lst) <= 87 or len(lst) < 82:
        return None
    return sorted(lst[82:87])[1]