def insert_after_character(s):
    return ''.join(('u' if c == 'X' else c for c in s))