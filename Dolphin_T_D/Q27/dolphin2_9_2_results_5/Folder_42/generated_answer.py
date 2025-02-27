def insert_after_index(given_list):
    result_list = given_list[:]
    for i in range(len(given_list)):
        if given_list[i] == 44:
            result_list.insert(i + 1, [40, 27])
    return result_list