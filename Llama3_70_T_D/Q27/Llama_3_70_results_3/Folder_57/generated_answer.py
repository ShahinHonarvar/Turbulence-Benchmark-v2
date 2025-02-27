def insert_after_index(input_list):
    index = input_list.index(90) + 1
    return input_list[:index] + [80] + input_list[index:]