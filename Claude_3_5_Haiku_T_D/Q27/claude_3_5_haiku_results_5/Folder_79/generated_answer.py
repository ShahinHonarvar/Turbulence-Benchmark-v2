def insert_after_index(input_list):
    if len(input_list) > 28:
        return input_list[:29] + [41, 69] + input_list[29:]
    else:
        return input_list