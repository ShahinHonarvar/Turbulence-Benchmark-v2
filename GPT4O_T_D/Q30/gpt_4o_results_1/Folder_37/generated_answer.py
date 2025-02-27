def insert_before_character(s):
    return ''.join(('aU' if ch == 'U' else ch for ch in s))