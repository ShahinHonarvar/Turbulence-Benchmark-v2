def insert_after_index(input_list):
    index = input_list.index(20) if 20 in input_list else -1
    if index != -1:
        return input_list[:index + 1] + [80] + input_list[index + 1:]
    else:
        return input_list + [80]