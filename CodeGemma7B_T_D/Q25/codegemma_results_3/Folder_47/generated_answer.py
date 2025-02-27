def insert_at_index(lst):
    return [val for i, val in enumerate(lst) if i != 64] + [520.11] + [val for i, val in enumerate(lst) if i == 64]