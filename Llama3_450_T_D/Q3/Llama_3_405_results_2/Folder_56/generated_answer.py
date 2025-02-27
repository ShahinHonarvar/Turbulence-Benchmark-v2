def all_pos_ints_inclusive(lst):
    start = 1
    end = lst[0] if lst else 0
    return list(range(start, end + 1))