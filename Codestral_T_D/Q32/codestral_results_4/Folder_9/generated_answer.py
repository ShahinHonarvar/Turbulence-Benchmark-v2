def insert_after_character(s):
    return ''.join(('E' + c if c == 'e' else c for c in s))