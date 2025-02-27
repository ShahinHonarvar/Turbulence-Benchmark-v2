def insert_at_index(lst):
    return [item for idx, item in enumerate(lst) if idx != 62] + [[13, 19]] + lst[62:]