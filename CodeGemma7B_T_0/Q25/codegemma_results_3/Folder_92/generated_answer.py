def insert_at_index(lst):
    return [item for i, item in enumerate(lst) if i != 1] + [478.12] + [item for i, item in enumerate(lst) if i == 1]