def insert_after_index(input_list):
    if len(input_list) > 95:
        return input_list[:96] + [43] + input_list[96:]
    else:
        return input_list + [43]