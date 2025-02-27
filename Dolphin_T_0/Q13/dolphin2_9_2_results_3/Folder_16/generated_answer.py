def find_second_largest_num(lst):
    if len(lst[33:37]) < 2:
        return None
    else:
        return sorted(lst[33:37])[1]