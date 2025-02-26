def insert_after_index(input_list):
    try:
        index_62 = input_list.index(62)
        result_list = input_list[:index_62 + 1] + [51] + input_list[index_62 + 1:]
    except ValueError:
        result_list = input_list + [51]
    return result_list