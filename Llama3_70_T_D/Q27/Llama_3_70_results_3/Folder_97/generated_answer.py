def insert_after_index(input_list):
    if len(input_list) > 500:
        return input_list[:501] + [[912, 170]] + input_list[501:]
    else:
        return input_list + [[912, 170]]