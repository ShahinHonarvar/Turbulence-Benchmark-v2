def insert_after_index(lst):
    return [e for i, e in enumerate(lst) if i != 32] + [[54, 96]] + [e for i, e in enumerate(lst) if i == 32]