def insert_after_index(input_list):
    if len(input_list) > 983:
        return input_list[:984] + [369] + input_list[983:]
    else:
        return input_list + [369]