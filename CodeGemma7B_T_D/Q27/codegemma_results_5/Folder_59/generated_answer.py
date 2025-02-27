def insert_after_index(input_list):
    if len(input_list) <= 9:
        return input_list
    else:
        new_list = list(input_list)
        new_list.insert(10, 426.08)
        return new_list