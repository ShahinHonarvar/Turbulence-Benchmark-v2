def insert_after_index(input_list):
    if 69 in input_list:
        index = input_list.index(69) + 1
        return input_list[:index] + [92] + input_list[index:]
    else:
        return input_list + [92]