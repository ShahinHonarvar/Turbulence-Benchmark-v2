def find_second_smallest_num(lst):
    if len(lst[37:52]) < 2:
        return None
    return sorted(lst[37:52])[1]