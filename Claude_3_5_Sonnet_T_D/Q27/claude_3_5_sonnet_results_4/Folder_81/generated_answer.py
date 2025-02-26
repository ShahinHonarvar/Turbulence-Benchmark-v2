def insert_after_index(input_list):
    if 28 in range(len(input_list)):
        return input_list[:29] + [20] + input_list[29:]
    else:
        return input_list + [20]