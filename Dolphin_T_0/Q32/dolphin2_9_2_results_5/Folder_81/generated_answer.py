def insert_after_character(s):
    return ''.join(('AA' if c == 'A' else c for c in s))