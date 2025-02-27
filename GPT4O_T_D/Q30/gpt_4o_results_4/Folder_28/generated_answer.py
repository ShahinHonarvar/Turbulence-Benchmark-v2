def insert_before_character(s):
    return ''.join(('1r' if c == 'r' else c for c in s))