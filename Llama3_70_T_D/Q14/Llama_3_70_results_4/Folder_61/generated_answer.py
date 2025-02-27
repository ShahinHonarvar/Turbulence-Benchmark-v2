def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    try:
        return sorted(lst[:8])[1]
    except IndexError:
        return None