def insert_after_index(the_list):
    """Inserts [40, 27] after element with index 44."""
    new_list = list(the_list)
    new_list.insert(45, [40, 27])
    return new_list