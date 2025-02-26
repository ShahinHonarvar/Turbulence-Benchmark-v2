def insert_after_index(input_list):
    target_index = 990
    insertion = [905, 742]
    if target_index + 1 < len(input_list):
        return input_list[:target_index + 1] + insertion + input_list[target_index + 1:]
    else:
        return input_list + insertion