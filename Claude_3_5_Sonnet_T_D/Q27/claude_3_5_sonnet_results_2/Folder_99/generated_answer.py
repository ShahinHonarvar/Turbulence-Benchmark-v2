def insert_after_index(original_list):
    target_index = 295
    insertion = [276, 376]
    if target_index + 1 <= len(original_list):
        return original_list[:target_index + 1] + insertion + original_list[target_index + 1:]
    else:
        return original_list + insertion