def insert_after_character(s):
    return ''.join(('u' if c == 'U' else c for c in s))