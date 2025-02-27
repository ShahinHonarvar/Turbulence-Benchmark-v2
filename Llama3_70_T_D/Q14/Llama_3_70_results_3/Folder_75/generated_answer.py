def find_second_smallest_num(lst):
    if len(lst[12:93]) < 2:
        return None
    return sorted(lst[12:93])[1]