def insert_after_index(lst):
    index_to_insert = 36
    sub_list_to_insert = [54, 13]
    return lst[:index_to_insert + 1] + sub_list_to_insert + lst[index_to_insert + 1:]