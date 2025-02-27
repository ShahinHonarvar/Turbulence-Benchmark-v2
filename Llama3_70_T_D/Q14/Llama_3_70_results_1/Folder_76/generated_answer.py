def find_second_smallest_num(lst):
    if len(lst[533:606]) < 2:
        return None
    else:
        return sorted(lst[533:606])[1]