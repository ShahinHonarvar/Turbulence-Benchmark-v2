def insert_at_index(lst):
    return [i if i < 761 else 925 if i == 761 else i + 1 for i in range(len(lst) + 1)]