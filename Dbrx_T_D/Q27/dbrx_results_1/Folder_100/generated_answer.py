def insert_after_index(lst):
    index_to_insert = 73
    element_to_insert = 418.88
    if index_to_insert < len(lst) - 1:
        index_to_insert += 1
    else:
        lst.append(element_to_insert)
        return lst
    lst = lst[:index_to_insert + 1] + [element_to_insert] + lst[index_to_insert + 1:]
    return lst