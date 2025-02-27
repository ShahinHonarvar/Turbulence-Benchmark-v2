def insert_after_index(lst):
    index_to_insert = lst.index(93) + 1
    sublist_to_insert = [33, 78]
    return lst[:index_to_insert] + sublist_to_insert + lst[index_to_insert:]