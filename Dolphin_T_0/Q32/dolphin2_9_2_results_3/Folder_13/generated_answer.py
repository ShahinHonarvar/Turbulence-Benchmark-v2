def insert_after_character(string):
    return ''.join(['N' if i == 'x' else c for i, c in zip(string, string + 'x')])