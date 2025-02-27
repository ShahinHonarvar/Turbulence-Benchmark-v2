def insert_after_character(x):
    return ''.join([c + 'n' if c == 'a' else c for c in x])