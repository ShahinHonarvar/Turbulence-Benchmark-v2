def insert_after_index(original_list):
    if len(original_list) > 42:
        return original_list[:43] + [53] + original_list[43:]
    return original_list + [53]