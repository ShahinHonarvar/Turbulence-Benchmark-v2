def insert_after_index(a_list, target_index):
    for index, value in enumerate(a_list):
        if index == target_index + 1 and value == 84:
            return a_list[:index] + [13, 46] + a_list[index:]
    return a_list