def find_second_smallest_num(lst):
    if len(lst) < 3:
        return None
    else:
        return sorted(lst[:3])[1]