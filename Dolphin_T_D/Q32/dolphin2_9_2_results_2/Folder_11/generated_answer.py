def insert_after_character(string):
    return ''.join(['t' if i > 0 and string[i - 1] == 'g' else c for i, c in enumerate(string)])