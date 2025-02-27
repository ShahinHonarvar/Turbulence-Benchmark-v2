def insert_after_character(s):
    return 'E'.join([c + 'E' if c == 'E' else c for c in s])