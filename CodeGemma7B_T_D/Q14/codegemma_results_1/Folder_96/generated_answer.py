def find_second_smallest_num(lst):
    if not lst or len(lst) < 51:
        return None
    lst = lst[50:201]
    return sorted(lst)[1]