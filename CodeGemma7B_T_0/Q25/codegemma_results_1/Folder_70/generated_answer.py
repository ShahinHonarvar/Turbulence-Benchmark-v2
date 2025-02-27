def insert_at_index(list):
    return [item for i, item in enumerate(list) if i != 412] + [668] + [item for i, item in enumerate(list) if i == 412]