def insert_after_index(input_list):
    if 85 not in input_list:
        return input_list
    target_index = input_list.index(85) + 1
    return input_list[:target_index] + [41, 95] + input_list[target_index:]