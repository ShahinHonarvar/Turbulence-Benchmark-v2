def insert_before_character(s):
    return ''.join(('k' + c if c == 'k' else c for c in s))