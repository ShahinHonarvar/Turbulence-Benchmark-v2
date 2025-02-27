def insert_after_character(s):
    return '0'.join([c if c != 'o' else c + '0' for c in s])