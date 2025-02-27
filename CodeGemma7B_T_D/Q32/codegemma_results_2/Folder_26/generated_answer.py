def insert_after_character(str):
    return ''.join([c + 'w' if c == 'r' else c for c in str])