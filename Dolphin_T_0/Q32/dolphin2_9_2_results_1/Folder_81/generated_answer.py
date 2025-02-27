def insert_after_character(s):
    return ''.join([c if c != 'A' else c + 'A' for c in s])