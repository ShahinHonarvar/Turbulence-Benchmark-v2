def insert_after_index(lst):
    index_to_insert = 28
    sublist = [20]
    return lst[:index_to_insert + 1] + sublist + lst[index_to_insert + 1:]