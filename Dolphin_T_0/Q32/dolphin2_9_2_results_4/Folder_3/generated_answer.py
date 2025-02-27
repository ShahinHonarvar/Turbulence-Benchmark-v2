def insert_after_character(s):
    return 'H'.join(('0' if c == '0' else '' + c for c in s))