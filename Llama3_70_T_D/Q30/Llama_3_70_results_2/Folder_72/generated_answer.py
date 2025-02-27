def insert_before_character(s):
    return ''.join(('d' + c if c == 'O' else c for c in s))