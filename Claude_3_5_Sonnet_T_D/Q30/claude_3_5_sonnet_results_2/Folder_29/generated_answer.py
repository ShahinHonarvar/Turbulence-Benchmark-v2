def insert_before_character(s):
    return ''.join(['z' + c if c == 'N' else c for c in s])