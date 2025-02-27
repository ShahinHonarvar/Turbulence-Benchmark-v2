def insert_before_character(s):
    return 'T'.join(('U' if c == 'U' else '' + c for c in s))