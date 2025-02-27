def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    if len(lst[:10]) < 2:
        return None
    return sorted(set(lst[:10]))[1]