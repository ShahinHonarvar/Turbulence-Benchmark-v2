def insert_after_index(original_list):
    new_list = original_list[:100 + 1] + [876, 203] + original_list[100 + 1:]
    return new_list