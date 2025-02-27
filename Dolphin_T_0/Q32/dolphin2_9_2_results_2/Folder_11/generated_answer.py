def insert_after_character(s):
    return ''.join([c if c != 'g' else c + 't' for c in s])