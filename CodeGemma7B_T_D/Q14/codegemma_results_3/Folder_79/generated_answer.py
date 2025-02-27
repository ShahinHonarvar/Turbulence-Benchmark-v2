def find_second_smallest_num(lst):
    if len(lst) < 5 or max(lst) - min(lst) < 2:
        return None
    return sorted(lst[1:6])[1]