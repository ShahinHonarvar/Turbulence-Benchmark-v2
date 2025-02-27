def insert_before_character(s):
    return ''.join(('G' + ch if ch == 'c' else ch for ch in s))