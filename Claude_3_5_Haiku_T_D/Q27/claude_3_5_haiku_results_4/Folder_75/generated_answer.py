def insert_after_index(input_list):
    result_list = input_list.copy()
    for i in range(len(result_list)):
        if result_list[i] == 99:
            result_list.insert(i + 1, 99)
    return result_list