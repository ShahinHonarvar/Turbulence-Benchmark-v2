def find_second_smallest_num(lst):
    if len(lst) < 88:
        return None
    return sorted(lst[30:88])[1]