def insert_before_character(s):
    return 'Q'.join(('O' if c == 'O' else '' for c in s)) + 'O' if s[-1] != 'O' else ''