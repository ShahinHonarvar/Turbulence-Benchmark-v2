def insert_after_index(input_list):
    insertion_index = 77
    if insertion_index <= len(input_list):
        return input_list[:insertion_index] + [15, 51] + input_list[insertion_index:]
    else:
        return input_list + [15, 51]