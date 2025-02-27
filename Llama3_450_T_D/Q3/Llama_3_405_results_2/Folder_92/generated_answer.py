def all_pos_ints_inclusive(lst):
    start = lst[0]
    end = lst[1]
    return [i for i in range(start, end + 1) if i > 0]