def insert_after_character(str):
    return ''.join([c + 'U' if c == 'u' else c for c in list(str)])