def insert_after_index(input_list):
    if len(input_list) > 101:
        return input_list[:101] + [876, 203] + input_list[101:]
    elif len(input_list) == 101:
        return input_list + [876, 203]
    else:
        return input_list