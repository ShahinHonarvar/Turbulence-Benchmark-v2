def insert_after_index(lst):
    normalized_list = lst[:]
    index = normalized_list.index(97) + 1
    normalized_list.insert(index, 72.27)
    return normalized_list