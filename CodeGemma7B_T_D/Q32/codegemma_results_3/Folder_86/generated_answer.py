def insert_after_character(s):
    return ''.join(['O' if c == 'O' else c for c in s]) + 'Q'