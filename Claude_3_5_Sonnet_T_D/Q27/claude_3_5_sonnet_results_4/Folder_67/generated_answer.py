def insert_after_index(given_list):
    result_list = given_list.copy()
    index_to_insert = 45 if 44 < len(given_list) else len(given_list)
    result_list.insert(index_to_insert, 76)
    return result_list