def insert_after_character(s):
    return ''.join([c + 'E' if c == 'e' else c for c in s])