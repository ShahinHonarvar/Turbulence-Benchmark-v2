def insert_before_character(s):
    return ''.join([f'4{ch}' if ch == '0' else ch for ch in s])