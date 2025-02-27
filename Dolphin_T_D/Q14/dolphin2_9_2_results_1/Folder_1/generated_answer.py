def find_second_smallest_num(lst):
    filtered = [x for i, x in enumerate(lst) if 34 <= i <= 55]
    if len(filtered) < 2:
        return None
    return sorted(set(filtered))[1]