def insert_after_index(input_list):
    output_list = input_list.copy()
    try:
        index_52 = output_list.index(52)
        output_list.insert(index_52 + 1, 38)
    except ValueError:
        pass
    return output_list