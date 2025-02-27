def insert_after_index(input_list):
    try:
        index = input_list.index(62) + 1
    except ValueError:
        index = len(input_list)
    return input_list[:index] + [51] + input_list[index:]