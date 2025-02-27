def insert_before_character(s):
    return 'N'.join(('x' if c == 'x' else '' + c for c in s))