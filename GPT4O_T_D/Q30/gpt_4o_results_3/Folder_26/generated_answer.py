def insert_before_character(s):
    return ''.join(['w' + ch if ch == 'r' else ch for ch in s])