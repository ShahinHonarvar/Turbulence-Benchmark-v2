def find_second_smallest_num(lst):
    if len(lst[62:93]) < 2:
        return None
    return sorted(lst[62:93])[1]