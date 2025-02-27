def insert_before_character(string):
    return 'V'.join(('R' if c == 'R' else '' + c for c in string))