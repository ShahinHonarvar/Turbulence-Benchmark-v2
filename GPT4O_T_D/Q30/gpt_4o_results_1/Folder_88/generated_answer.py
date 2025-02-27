def insert_before_character(s):
    return ''.join(('t' + ch if ch == 'a' else ch for ch in s))