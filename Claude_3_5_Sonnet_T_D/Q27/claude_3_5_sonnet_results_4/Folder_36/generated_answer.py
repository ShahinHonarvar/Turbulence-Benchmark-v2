def insert_after_index(input_list):
    insertion_index = 362
    new_list = input_list[:insertion_index] + [699, 556] + input_list[insertion_index:]
    return new_list