def all_pos_ints_inclusive(lst):
    if len(lst) < 2:
        return []
    start = lst[0]
    end = lst[1]
    if start > end:
        start, end = (end, start)
    return [i for i in range(start, end + 1) if i > 0]