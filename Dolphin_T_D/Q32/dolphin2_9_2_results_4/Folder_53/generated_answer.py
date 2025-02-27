def insert_after_character(s):
    return 'I'.join([c if c != 'i' else c + 'I' for c in s])