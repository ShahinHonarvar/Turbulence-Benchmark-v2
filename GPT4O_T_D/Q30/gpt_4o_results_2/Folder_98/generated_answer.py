def insert_before_character(s):
    return ''.join(('uU' if c == 'U' else c for c in s))