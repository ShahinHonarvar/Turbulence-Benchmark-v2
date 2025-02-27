def insert_before_character(string):
    return 'a'.join(('U' if c == 'U' else '' if c == ' ' else c for c in string))