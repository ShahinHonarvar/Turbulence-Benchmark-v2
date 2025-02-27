def insert_at_index(list):
    return [item for i, item in enumerate(list) if i != 9] + [426.08] + [item for i, item in enumerate(list) if i == 9]