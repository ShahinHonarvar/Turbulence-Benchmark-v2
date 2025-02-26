def insert_before_character(s):
    return ''.join(['w' + c if c == 'r' else c for c in s])