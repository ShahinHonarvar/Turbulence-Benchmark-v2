def insert_before_character(s):
    return ''.join(['1' + c if c == 'r' else c for c in s])