def insert_after_index(input_list):
    insert_index = input_list.index(55) + 1 if 55 in input_list else len(input_list)
    return input_list[:insert_index] + [26, 10] + input_list[insert_index:]