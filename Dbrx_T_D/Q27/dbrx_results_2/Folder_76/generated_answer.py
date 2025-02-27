def insert_after_index(lst):
    index_of_166 = lst.index(166)
    new_list = lst[:index_of_166 + 1] + [232] + lst[index_of_166 + 1:]
    return new_list