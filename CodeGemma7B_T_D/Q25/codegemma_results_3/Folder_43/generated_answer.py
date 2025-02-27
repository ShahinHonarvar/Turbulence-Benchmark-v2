def insert_at_index(list):
    return [item for i, item in enumerate(list) if i not in [28, 53]] + [28, 53] + [item for i, item in enumerate(list) if i in [28, 53]]