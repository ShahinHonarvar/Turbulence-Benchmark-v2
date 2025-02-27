def insert_before_character(s):
    return 'V'.join(('P' if c == 'P' else '' + c for c in s))