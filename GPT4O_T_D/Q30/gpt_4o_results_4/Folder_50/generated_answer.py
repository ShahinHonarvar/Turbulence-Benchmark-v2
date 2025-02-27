def insert_before_character(s):
    return ''.join(('u' + ch if ch == 't' else ch for ch in s))