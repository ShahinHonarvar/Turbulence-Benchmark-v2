def find_second_largest_num(lst):
    if len(lst) < 4:
        return None
    return sorted(lst[0:4])[1]