def insert_at_index(list):
    return [item for i, item in enumerate(list) if i != 564] + [149] + [item for i, item in enumerate(list) if i == 564]