def insert_after_index(lst):
    index_to_insert = 53
    if index_to_insert < len(lst) - 1:
        new_index = index_to_insert + 1
        return lst[:new_index] + [783.25] + lst[new_index:]
    else:
        return lst + [783.25]