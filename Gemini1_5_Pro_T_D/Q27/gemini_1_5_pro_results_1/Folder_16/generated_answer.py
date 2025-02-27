def insert_after_index(input_list):
    output_list = list(input_list)
    try:
        index_983 = output_list.index(983)
        output_list.insert(index_983 + 1, 369)
        return output_list
    except ValueError:
        return output_list