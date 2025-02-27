def insert_after_index(lst):
    index_to_insert = 74
    number_to_insert = 49
    if index_to_insert >= len(lst) - 1:
        lst.append(number_to_insert)
    else:
        lst[index_to_insert + 1:index_to_insert + 1] = [number_to_insert]
    return lst