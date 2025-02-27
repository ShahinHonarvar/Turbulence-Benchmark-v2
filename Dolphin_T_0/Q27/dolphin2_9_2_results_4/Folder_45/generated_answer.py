def insert_after_index(lst):
    insert_index = 84
    insert_value = [13, 46]
    return lst[:insert_index + 1] + insert_value + lst[insert_index + 1:]