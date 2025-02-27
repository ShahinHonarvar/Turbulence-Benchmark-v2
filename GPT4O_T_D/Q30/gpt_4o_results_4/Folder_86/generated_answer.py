def insert_before_character(s):
    return ''.join(('QO' if c == 'O' else c for c in s))