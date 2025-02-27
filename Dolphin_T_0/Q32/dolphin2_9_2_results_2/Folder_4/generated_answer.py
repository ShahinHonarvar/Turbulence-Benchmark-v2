def insert_after_character(s):
    return '6'.join(('a' if c == 'a' else '' + c for c in s)) + ('6' if s[-1] == 'a' else '')