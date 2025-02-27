def insert_before_character(string):
    return ''.join(['l' if i > 0 and string[i - 1] == 'K' or string[i] == 'K' else c for i, c in enumerate(string)])