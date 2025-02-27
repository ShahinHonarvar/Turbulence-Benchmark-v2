def insert_after_character(string):
    return ''.join(['5' if i != 0 and string[i - 1] == ' ' else c for i, c in enumerate(string)])