def insert_before_character(s):
    return 'G'.join(('c' if c == 'c' else '' + c for c in s))