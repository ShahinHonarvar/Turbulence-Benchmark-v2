def insert_before_character(string):
    return 'u'.join(('X' if c == 'X' else str(c) for c in string))