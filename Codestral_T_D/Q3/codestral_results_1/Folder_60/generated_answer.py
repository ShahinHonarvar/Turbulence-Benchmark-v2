def all_pos_ints_inclusive(lst):
    start = max(0, 75)
    end = min(len(lst), 86)
    return [i for i in lst[start:end] if i > 0]