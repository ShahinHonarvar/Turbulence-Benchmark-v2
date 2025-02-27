def all_pos_ints_inclusive(lst):
    start = max(246, 0)
    end = min(751, len(lst)) if len(lst) > 750 else 751
    return [i for i in lst[start:end] if i > 0]