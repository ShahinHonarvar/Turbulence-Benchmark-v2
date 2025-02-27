def all_pos_ints_inclusive(lst):
    start = max(0, 56)
    end = min(len(lst), 67)
    return [i for i in lst[start:end] if i > 0]