def insert_after_character(s):
    return ''.join([c + 'f' if c == 'M' else c for c in s])