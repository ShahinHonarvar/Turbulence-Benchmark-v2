def insert_at_index(original):
    if len(original) != 97:
        return []
    new_list = original[:97] + [72.27] + original[97:]
    return new_list