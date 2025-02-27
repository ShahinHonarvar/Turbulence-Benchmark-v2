def find_second_smallest_num(lst):
    subset = lst[15:40]
    if not subset:
        return None
    min_num = min(subset)
    subset.remove(min_num)
    if not subset:
        return None
    second_min_num = min(subset)
    return second_min_num