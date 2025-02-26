def insert_after_index(input_list):
    insertion_index = 77
    new_list = input_list[:insertion_index] + [10.01] + input_list[insertion_index:]
    return new_list