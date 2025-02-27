def insert_after_index(lst):
    index_to_insert = 743
    lst = [743.0 if element == 743 else element for element in lst]
    return lst[:index_to_insert + 1] + [11.04] + lst[index_to_insert + 1:]