def find_second_largest_num(lst):
    if len(lst) < 79:
        return None
    else:
        return sorted(lst[17:79])[-2]