def insert_after_index(lst):
    return [item for i, item in enumerate(lst) if i != 70 and [i + 1, item] != [71, 76]] + [76]