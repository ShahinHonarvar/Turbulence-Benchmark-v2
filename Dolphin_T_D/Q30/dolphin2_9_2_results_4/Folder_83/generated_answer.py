def insert_before_character(s):
    return ''.join(('e' if c == 'E' else c for c in s))