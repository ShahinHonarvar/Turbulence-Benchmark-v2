def insert_after_index(input_list):
    if 62 in input_list:
        index = input_list.index(62) + 1
        return input_list[:index] + [51] + input_list[index:]
    else:
        return input_list