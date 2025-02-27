def insert_before_character(s):
    return 'V'.join(('P' if c == 'P' else '' + s for c in s))