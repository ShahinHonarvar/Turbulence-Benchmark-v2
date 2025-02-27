def insert_at_index(list):
    return [item for idx, item in enumerate(list) if idx != 42] + [53] + [item for idx, item in enumerate(list) if idx == 42]