def find_second_smallest_num(lst):
    if len(lst) < 4:
        return None
    return sorted(lst[:4])[1]