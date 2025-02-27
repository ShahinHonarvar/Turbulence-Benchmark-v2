def insert_after_character(s):
    return ''.join([c if c != 'H' else c + 'n' for c in s])