def insert_before_character(s):
    return 't'.join(('a' if c == 'a' else '' + c for c in s))