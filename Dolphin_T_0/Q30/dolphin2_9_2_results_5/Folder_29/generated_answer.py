def insert_before_character(s):
    return 'z'.join(('N' if c == 'N' else '' if c == 'z' else c for c in s))