def insert_before_character(s):
    return ''.join(['u' + c if c == 'X' else c for c in s])