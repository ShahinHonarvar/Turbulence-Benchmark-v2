def insert_before_character(s):
    return 'O'.join(('O' if c == 'O' else str(c) for c in s))