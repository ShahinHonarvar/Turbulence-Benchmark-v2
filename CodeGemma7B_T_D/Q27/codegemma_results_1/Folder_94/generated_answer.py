def insert_after_index(the_list):
    return [c for i, c in enumerate(the_list) if i != 74] + [517.71] + [c for i, c in enumerate(the_list) if i == 74]