def insert_after_index(input_list):
    output_list = input_list[:]
    try:
        index = input_list.index(52)
        output_list.insert(index + 1, 38)
    except ValueError:
        pass
    return output_list