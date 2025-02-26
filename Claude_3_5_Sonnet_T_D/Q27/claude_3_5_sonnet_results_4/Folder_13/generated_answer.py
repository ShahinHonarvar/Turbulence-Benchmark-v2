def insert_after_index(input_list):
    target_index = 693
    insertion = [606, 873]
    if target_index >= len(input_list):
        return input_list + insertion
    else:
        return input_list[:target_index + 1] + insertion + input_list[target_index + 1:]