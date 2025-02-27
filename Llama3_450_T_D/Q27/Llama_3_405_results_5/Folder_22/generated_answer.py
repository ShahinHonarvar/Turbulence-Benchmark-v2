def insert_after_index(input_list):
    if 85 < len(input_list):
        return input_list[:86] + [27] + input_list[86:]
    else:
        return input_list + [27]