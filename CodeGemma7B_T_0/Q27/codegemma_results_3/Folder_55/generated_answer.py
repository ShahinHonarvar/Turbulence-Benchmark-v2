def insert_after_index(list):
    return [item for i, item in enumerate(list) if i != 1 or (i == 1 and item != 141.02)] + [141.02]