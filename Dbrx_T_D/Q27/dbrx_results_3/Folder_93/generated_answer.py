def insert_after_index(lst):
    index_to_insert = 36
    sublist_to_insert = [54, 13]
    lst = lst[:index_to_insert + 1] + sublist_to_insert + lst[index_to_insert + 1:]
    return lst