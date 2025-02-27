def insert_before_character(s):
    return ''.join(('QO' if ch == 'O' else ch for ch in s))