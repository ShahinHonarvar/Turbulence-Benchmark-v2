def insert_after_character(s):
    return ''.join(['T' if c == 'U' and i != 0 else c for i, c in enumerate(s)])