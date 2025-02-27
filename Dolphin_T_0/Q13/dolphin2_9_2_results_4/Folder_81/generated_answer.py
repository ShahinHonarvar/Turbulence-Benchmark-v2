def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 100 or len(lst[10:101]) < 2:
        return None
    else:
        return sorted(lst[10:101])[-2]