def insert_before_character(s):
    return ''.join(['Z' + c if c == 'C' else c for c in s])