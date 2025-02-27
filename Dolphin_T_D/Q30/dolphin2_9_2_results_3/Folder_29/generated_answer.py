def insert_before_character(s):
    return ''.join(('z' if c == 'N' else c for c in s))