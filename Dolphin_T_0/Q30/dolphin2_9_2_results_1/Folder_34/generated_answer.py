def insert_before_character(s):
    return 'a' + ''.join(('a' if c.upper() == 'A' else c for c in s))