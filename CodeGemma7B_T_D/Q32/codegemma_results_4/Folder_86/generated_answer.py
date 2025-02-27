def insert_after_character(s):
    return ''.join([c + 'Q' if c == 'O' else c for c in s])