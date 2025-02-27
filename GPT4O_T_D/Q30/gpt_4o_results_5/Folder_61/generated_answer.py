def insert_before_character(s):
    return ''.join(('0e' if c == 'e' else c for c in s))