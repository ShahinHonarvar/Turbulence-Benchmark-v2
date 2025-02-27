def insert_before_character(s):
    return ''.join(('0a' if ch == 'a' else ch for ch in s))