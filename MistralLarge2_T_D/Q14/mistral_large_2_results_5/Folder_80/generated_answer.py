def find_second_smallest_num(lst):
    subset = lst[30:88]
    if len(subset) < 2:
        return None
    return sorted(subset)[1]