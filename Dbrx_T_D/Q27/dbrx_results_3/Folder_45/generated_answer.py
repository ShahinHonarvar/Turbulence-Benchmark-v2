def insert_after_index(lst):
    index_to_insert = lst.index(84) + 1
    new_element = [13, 46]
    lst = lst[:index_to_insert] + new_element + lst[index_to_insert:]
    return lst