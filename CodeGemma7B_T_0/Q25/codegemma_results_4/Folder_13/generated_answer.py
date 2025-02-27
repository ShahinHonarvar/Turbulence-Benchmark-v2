def insert_at_index(list):
    return [item for i, item in enumerate(list) if i != 693] + [606, 873] + [item for i, item in enumerate(list) if i == 693]