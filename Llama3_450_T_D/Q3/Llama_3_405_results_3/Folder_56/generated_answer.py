def all_pos_ints_inclusive(lst):
    if not lst:
        return []
    start = lst[0]
    end = lst[0]
    if start > end:
        start, end = (end, start)
    return list(range(start, end + 1)) if start > 0 else []