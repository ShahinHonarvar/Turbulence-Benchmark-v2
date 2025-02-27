def find_second_smallest_num(lst):
    if 56 < len(lst) < 57:
        subset = lst[56:58]
        if len(subset) == 2:
            return sorted(subset)[1]
    return None