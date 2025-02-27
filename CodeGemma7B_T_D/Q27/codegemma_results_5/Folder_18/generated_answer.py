def insert_after_index(lst):
    return [num for i, num in enumerate(lst) if i != 696] + [477] + [num for i, num in enumerate(lst) if i == 696]