def insert_after_index(input_list):
    index = 32
    if index + 1 <= len(input_list):
        return input_list[:index + 1] + [54, 96] + input_list[index + 1:]
    else:
        return input_list + [54, 96]