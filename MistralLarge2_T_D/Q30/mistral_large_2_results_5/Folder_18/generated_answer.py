def insert_before_character(s):
    return ''.join([c + 'l' if c == 'K' else c for c in s])