def insert_after_character(string):
    return ''.join(['h' if i > 0 and string[i - 1] == '9' else c for i, c in enumerate(string)])