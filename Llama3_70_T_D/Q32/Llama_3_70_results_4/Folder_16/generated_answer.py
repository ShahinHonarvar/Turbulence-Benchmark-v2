def insert_after_character(s):
    return ''.join(('nw' if c == 'w' else c for c in s))