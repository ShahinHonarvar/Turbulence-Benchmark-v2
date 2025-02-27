def insert_after_character(string):
    return ''.join(['F' if i > 0 and string[i - 1] == '4' else c for i, c in enumerate(string)])