def insert_after_character(s):
    return ''.join([c if c != 'B' else c + 'N' for c in s])