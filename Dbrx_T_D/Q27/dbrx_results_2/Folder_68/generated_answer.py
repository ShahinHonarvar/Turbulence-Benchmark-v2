def insert_after_index(lst):
    index_to_insert = 7 + 1
    sublist_to_insert = [1, 7]
    return lst[:index_to_insert] + sublist_to_insert + lst[index_to_insert:]