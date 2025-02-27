def insert_before_character(s):
    return 'o'.join(('O' if c == 'O' else '' if c == 'o' else c for c in s))