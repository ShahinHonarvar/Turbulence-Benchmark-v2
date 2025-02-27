def insert_before_character(s):
    return '0'.join(('e' if c == 'e' else str(c) for c in s))