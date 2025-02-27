def insert_at_index(input_list):
    if len(input_list) >= 93:
        return input_list[:93] + [33, 78] + input_list[93:]
    else:
        raise IndexError('The list does not have an index 93 to insert the elements.')