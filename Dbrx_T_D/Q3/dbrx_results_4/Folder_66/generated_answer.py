def all_pos_ints_inclusive(lst):
    start = 50
    end = 54
    if len(lst) <= end:
        return []
    else:
        return [i for i in lst[start:end + 1] if i > 0]