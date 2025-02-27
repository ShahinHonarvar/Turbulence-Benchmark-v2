def insert_after_index(lst):
    index_to_insert = 76
    if index_to_insert < len(lst) - 1:
        return lst[:index_to_insert + 1] + [10.01] + lst[index_to_insert + 1:]
    else:
        return lst + [10.01]