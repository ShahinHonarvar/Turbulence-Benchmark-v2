def insert_after_character(s):
    return ''.join(('z' if c == 'N' else c for c in s)) + 'z'