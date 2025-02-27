def insert_at_index(list):
    return [item for i, item in enumerate(list) if i != 70 or (i == 70 and item != 185.43)] + [185.43]