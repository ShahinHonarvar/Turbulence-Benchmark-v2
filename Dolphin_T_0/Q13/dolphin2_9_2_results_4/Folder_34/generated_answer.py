def find_second_largest_num(lst):
    if len(lst) < 62 or len(lst) > 16:
        return None
    else:
        return sorted(lst[16:62])[-2]