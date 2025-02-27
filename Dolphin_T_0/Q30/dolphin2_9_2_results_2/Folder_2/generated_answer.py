def insert_before_character(x):
    return 'Z' + x if x[0] == 'C' else x[0] + insert_before_character(x[1:]) if x else ''