def insert_after_character(string):
    return ''.join(['A' if i > 0 and string[i - 1] == 'a' else c for i, c in enumerate(string)])