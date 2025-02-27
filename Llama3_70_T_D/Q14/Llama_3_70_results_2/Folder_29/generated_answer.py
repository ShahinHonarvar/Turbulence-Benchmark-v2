def find_second_smallest_num(lst):
    if len(lst) < 99:
        return None
    else:
        return sorted(lst[55:99])[1]