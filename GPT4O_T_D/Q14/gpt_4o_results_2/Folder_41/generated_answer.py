def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    window = lst[4:5]
    if len(window) < 2:
        return None
    first_min = min(window)
    window.remove(first_min)
    second_min = min(window)
    return second_min