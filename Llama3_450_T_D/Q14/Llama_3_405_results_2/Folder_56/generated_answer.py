def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    return sorted(lst[:1])[1]