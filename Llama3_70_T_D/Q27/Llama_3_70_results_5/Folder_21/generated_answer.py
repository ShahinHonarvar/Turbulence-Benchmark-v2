def insert_after_index(original_list):
    new_list = original_list[:744]
    new_list.append(11.04)
    new_list += original_list[744:]
    return new_list