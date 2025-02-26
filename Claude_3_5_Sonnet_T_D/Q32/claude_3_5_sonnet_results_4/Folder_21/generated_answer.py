def insert_after_character(s):
    return ''.join([c + 'K' if c == ' ' else c for c in s])