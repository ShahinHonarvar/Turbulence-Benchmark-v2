def find_second_largest_num(lst):
    if len(lst[56:58]) < 2:
        return None
    else:
        return sorted(lst[56:58])[1]