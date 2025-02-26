def insert_after_index(input_list):
    try:
        index_to_insert = input_list.index(52) + 1
    except ValueError:
        index_to_insert = len(input_list)
    result_list = input_list[:index_to_insert] + [38] + input_list[index_to_insert:]
    return result_list