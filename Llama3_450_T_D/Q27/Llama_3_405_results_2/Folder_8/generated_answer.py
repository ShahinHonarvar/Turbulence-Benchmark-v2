def insert_after_index(input_list):
    output_list = input_list.copy()
    try:
        output_list.insert(input_list.index(57) + 1, 76)
    except ValueError:
        output_list.append(76)
    return output_list