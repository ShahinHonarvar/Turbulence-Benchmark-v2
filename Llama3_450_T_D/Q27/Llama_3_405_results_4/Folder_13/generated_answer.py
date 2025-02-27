def insert_after_index(input_list):
    if 693 < len(input_list):
        return input_list[:694] + [606, 873] + input_list[694:]
    else:
        return input_list + [606, 873]