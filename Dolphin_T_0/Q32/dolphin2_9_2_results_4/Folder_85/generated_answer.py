def insert_after_character(s):
    return 'a'.join([c if c != 'o' else c + 'a' for c in s])