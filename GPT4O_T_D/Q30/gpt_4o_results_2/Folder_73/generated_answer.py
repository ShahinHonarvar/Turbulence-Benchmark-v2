def insert_before_character(s):
    return ''.join(('V' + ch if ch == 'R' else ch for ch in s))