def insert_after_index(lst):
    index_to_insert = 97
    if index_to_insert < len(lst) - 1:
        index_to_insert += 1
    else:
        return lst + [72.27]
    return lst[:index_to_insert] + [72.27] + lst[index_to_insert:]