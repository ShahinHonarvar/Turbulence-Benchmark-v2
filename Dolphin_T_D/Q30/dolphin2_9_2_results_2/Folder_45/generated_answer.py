def insert_before_character(s):
    return 'O'.join(('O' + s if c == 'O' else s for c in s))