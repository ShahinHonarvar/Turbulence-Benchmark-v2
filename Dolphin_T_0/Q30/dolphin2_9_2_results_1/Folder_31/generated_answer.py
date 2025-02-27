def insert_before_character(s):
    return ''.join(('N' if c == 'B' else c for c in s))