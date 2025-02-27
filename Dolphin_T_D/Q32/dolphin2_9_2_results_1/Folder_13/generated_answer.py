def insert_after_character(string):
    return ''.join(['N' if i > 0 and string[i - 1] == 'x' else c for i, c in enumerate(string)])