def insert_after_index(given_list):
    index_44 = given_list.index(44) if 44 in given_list else -1
    if index_44 != -1:
        given_list.insert(index_44 + 1, [40, 27])
    return given_list