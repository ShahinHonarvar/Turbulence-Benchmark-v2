def insert_before_character(s):
    return ''.join(('W' + ch if ch == 'a' else ch for ch in s))