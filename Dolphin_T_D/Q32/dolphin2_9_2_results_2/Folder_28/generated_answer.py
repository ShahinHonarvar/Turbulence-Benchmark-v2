def insert_after_character(s):
    return ''.join(('1' if c == 'r' else c for c in s)) + '1'