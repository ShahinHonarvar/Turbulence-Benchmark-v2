def insert_after_character(s):
    return 'M'.join([c if c != '9' else '9M' for c in s])