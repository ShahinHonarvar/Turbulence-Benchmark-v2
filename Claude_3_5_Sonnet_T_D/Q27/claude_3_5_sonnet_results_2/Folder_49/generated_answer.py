def insert_after_index(given_list):
    index_to_insert = given_list.index(38) + 1
    result_list = given_list[:index_to_insert] + [27, 34] + given_list[index_to_insert:]
    return result_list