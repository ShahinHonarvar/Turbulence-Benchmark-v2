def insert_before_character(s):
    return 'e'.join(('e' if c == 'E' else '' + c for c in s))