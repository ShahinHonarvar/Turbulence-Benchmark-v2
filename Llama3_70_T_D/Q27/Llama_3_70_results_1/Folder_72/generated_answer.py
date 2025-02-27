def insert_after_index(input_list):
    if len(input_list) > 24:
        return input_list[:25] + [98, 22] + input_list[25:]
    else:
        return input_list + [98, 22]