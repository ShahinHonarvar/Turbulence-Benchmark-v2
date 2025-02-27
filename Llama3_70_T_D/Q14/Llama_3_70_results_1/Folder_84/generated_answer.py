def find_second_smallest_num(lst):
    if len(lst) < 81:
        return None
    return sorted(set(lst[40:81]))[1] if len(set(lst[40:81])) > 1 else None