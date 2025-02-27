def insert_after_character(s):
    return ''.join([c + 'X' if c == ' ' else c for c in s])