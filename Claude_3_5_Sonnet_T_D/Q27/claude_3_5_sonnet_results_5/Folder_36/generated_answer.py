def insert_after_index(input_list):
    new_list = input_list.copy()
    insertion_index = 362 if len(new_list) > 361 else len(new_list)
    new_list[insertion_index:insertion_index] = [699, 556]
    return new_list