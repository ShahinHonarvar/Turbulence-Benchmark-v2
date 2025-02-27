def insert_after_character(s):
    return ''.join(('T' if c == 'E' else c for c in s)) + 'T'