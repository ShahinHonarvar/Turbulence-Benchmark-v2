def find_second_largest_num(lst):
    if len(lst) < 99:
        return None
    return sorted(lst[55:99])[-2]