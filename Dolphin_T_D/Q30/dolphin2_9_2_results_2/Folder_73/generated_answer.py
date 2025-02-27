def insert_before_character(s):
    return 'V'.join(('R' if c == 'R' else '' + c for c in s))