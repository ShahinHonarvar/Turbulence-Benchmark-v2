def all_pos_ints_inclusive(lst):
    if not lst:
        return []
    start = 0
    end = lst[0]
    return [i for i in range(start, end + 1) if i > 0]