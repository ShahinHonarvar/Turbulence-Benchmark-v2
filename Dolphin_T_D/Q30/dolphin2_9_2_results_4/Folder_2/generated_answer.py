def insert_before_character(string):
    return ''.join(['Z' if c == 'C' else string[i] for i, c in enumerate(string)])