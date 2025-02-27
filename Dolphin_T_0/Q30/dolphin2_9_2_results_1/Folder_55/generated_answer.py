def insert_before_character(s):
    return 'U'.join(('U' if c == 'u' else c for c in s))