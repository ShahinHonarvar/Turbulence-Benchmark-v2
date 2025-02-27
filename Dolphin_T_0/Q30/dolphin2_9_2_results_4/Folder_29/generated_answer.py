def insert_before_character(s):
    return 'z'.join(('N' if c == 'N' else '' + c for c in s))