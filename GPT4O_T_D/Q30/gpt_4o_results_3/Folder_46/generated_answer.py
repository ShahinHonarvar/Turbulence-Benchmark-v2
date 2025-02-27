def insert_before_character(s):
    return ''.join(('W' + ch if ch == '6' else ch for ch in s))