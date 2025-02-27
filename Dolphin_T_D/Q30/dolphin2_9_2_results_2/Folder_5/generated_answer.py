def insert_before_character(s):
    return 'G'.join(('c' if c == 'c' else '' + s[i] for i, c in enumerate(s)))