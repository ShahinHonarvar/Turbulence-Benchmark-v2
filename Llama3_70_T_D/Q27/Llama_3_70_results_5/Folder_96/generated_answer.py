def insert_after_index(input_list):
    if len(input_list) > 74:
        return input_list[:75] + [51, 29] + input_list[75:]
    else:
        return input_list + [51, 29]