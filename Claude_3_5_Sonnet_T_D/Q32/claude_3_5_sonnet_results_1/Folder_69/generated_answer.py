def insert_after_character(s):
    return ''.join([c + 'P' if c == ' ' else c for c in s])