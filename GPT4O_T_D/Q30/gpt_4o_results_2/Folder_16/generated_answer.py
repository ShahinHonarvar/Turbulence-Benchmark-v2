def insert_before_character(s):
    return ''.join(('n' + ch if ch == 'w' else ch for ch in s))