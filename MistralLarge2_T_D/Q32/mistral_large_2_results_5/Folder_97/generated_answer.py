def insert_after_character(s):
    return ''.join([c + 'h' if c == 'o' else c for c in s])